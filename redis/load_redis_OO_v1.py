#!/usr/bin/python
"""
load_redis.py
------------------------
- Script to load urls data into a Redis instance from .txt files
- Only to be used for bulk inserts of urls (no priority/notes data exists in the .txt files)
- Usage:
    >>> f = Files()
    >>> f.add('/Users/Mike/data/tmp/recent-sites-redis-inserts/','foo.txt')
    >>> f
    <__main__.Files object at 0x101573ac8>
    >>> for time_added, category, site_name, url in f.gen_all_site_info():
    ...     print(time_added, category, site_name, url)
    ... 
    18:52-02/03/2018 foo gkhsdgh http://gkhsdgh.com/egohsnsf
    18:52-02/03/2018 foo example http://example.com/test.html
    18:52-02/03/2018 foo example http://example.com/bar
    18:52-02/03/2018 foo example http://example.com/
    >>>
    >>> f.print_all_site_info()
    18:52-02/03/2018 foo gkhsdgh http://gkhsdgh.com/egohsnsf
    18:52-02/03/2018 foo example http://example.com/test.html
    18:52-02/03/2018 foo example http://example.com/bar
    18:52-02/03/2018 foo example http://example.com/

"""

class Files:
    """ All File objects """
    
    __slots__ = ('objs',)
    
    def __init__(self):
        self.objs = None
        
    def __len__(self):
        if self.objs is None: return 0
        else: return len(self.objs)
        
    def site_count(self):
        if self.objs is None: return 0
        else:
            length = 0
            for obj in self.__iter__():
                length += obj.count()
        return length
    
    def add(self, filepath, filename):
        file_obj = File().add(filepath, filename)
        if self.objs is None: self.objs = [file_obj]
        else: self.objs.append(file_obj)
        
    def __iter__(self):
        if self.objs is not None:
            for obj in self.objs:
                yield obj
        else: raise ValueError('No data in Tree object.')
        
    def gen_all_site_info(self):
        for f_obj in self.__iter__():
            for time_added, category, site_name, url in f_obj._iter_contents__():
                yield time_added, category, site_name, url
                
    def print_all_site_info(self):
        for time_added, category, site_name, url in self.gen_all_site_info():
            print(time_added, category, site_name, url)


class File:
    """ .txt file metadata and actual site contents (Site object) """
    
    __slots__ = ('file_path', 'file_contents', 'time_added', 'category')
    
    def __init__(self):
        self.file_path = None
        self.file_contents = None
        self.time_added = None
        self.category = None
        
    def add(self, file_path, file_name):
        from datetime import datetime as dt
        if isinstance(file_path,str) and isinstance(file_name,str):
            self.file_path = file_path + file_name
            self.category = file_name.rstrip('.txt')
            self._open()
            self.time_added = dt.now().strftime('%H:%M-%m/%d/%Y')
            return self
        else:
            raise TypeError("file_path or file_name variable not type str")
            
    def count(self):
        if self.file_contents is None: return 0
        else: return len(self.file_contents)
        
    def _open(self):
        if self.file_contents is None: self.file_contents = []
        with open(self.file_path,'r') as f:
            for line in f.readlines():
                site = Site()
                site.add(line.rstrip('\r\n'))
                self.file_contents.append(site.get())
        self.file_contents.reverse()
                
    def _get_contents(self):
        return self.file_contents
        
    def __iter__(self):
        if self.file_contents is None:
            raise ValueError('No file contents in this object'+str(self))
        else:
            for obj in self.file_contents:
                yield obj
    
    def _iter_contents__(self):
        for content in self.__iter__():
            yield (self.time_added, self.category, content.name, content.url )

class Site:
    """ Data for individual sites """
    
    __slots__ = ('url','name')
    
    def __init__(self):
        self.url = None
        self.name = None
    
    def add(self, content):
        self.url = content
        self.name = content.lstrip('http://').lstrip('www.').split('.')[0]
        return True
        
    def get(self):
        return self


def load_data(fp):
    """ Get data from .txt files in a directory and add them to a FilesTree object"""
    import os
    files_list = os.listdir(fp)
    if len(files_list) < 1:
        print('No files exist! Exiting')
        exit()
    else:
        bulk_files = Files()
        for filename in os.listdir(fp):
            if '.txt' in filename:
                bulk_files.add(fp, filename)
        return bulk_files
        
def insert_redis(FilesObject, redis_instance):
    """ Load from a FilesTree object into redis """
    set_added, hash_added = 0,0
    if FilesObject.__len__() == 0: raise ValueError('No files in tree object.')
    for idx, time_added, category, site_name, url in enumerate(FilesObject.gen_all_site_info()):
        set_added += redis_instance.sadd(category, url)
        redis_hash_dict = { \
                                'time_added' : time_added \
                                , 'category' : category \
                                , 'site_name' : site_name \
                                , 'notes' : '' \
                                , 'priority' : 0 \
                            }
        if redis_instance.hmset(url, redis_hash_dict) == "OK": hash_added +=1
    return idx, set_added, hash_added

def main(filepath = './app/data/', redis_host = 'recent-sites-redis' , redis_port = 6379):
    import redis
    redis_instance = redis.Redis(host=redis_host, port=redis_port)
    try:
        redis_instance.ping()
    except ConnectionError as e:
        print('Could not connect to Redis -> host: {h} --port: {p}'.format(h=redis_host,p=redis_port))
        exit(500)
    else:
        parsed, set_added, hash_added = insert_redis(load_data(filepath), redis_instance)
        print('Set Adds: {s:,d} / Hash Adds: {h:,d}'.format(p=parsed, s=set_added, h=hash_added))

if __name__ == '__main__':
    main()
