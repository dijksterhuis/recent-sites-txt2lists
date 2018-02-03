#!/usr/bin/python
"""
load_redis.py
------------------------
- Script to initially load urls into a Redis instance from .txt files
- Only to be used for bulk inserts of urls (no priority fields etc.)
"""

class FilesTree:
    """ Object to hold all the FileObjects """
    def __init__(self):
        self.objs = None
        
    def add(self, obj):
        if self.objs is None: self.objs = [obj]
        else: self.objs.append(obj)
        
    def __iter__(self):
        if self.objs is not None:
            for i in self.objs:
                yield i

class FileObject:
    """ An Object to hold .txt file data """
    def __init__(self):
        self.file_path = None
        self.file_contents = None
        self.time_added = None
        self.category = None
        
    def add(self, file_path,filename):
        from datetime import datetime as dt
        if isinstance(file_path,str):
            self.file_path = file_path
            self.category = filename.rstrip('.txt')
            self._open(self.file_path + filename)
            self.time_added = dt.now().strftime('%H:%M-%m/%d/%Y')
            return self
        else:
            raise TypeError("file_path variable not type str")
            
    def _open(self,fp):
        with open(fp,'r') as f:
            self.file_contents = [ line.rstrip('\n\r') for line in f.readlines() ]
            self.file_contents.reverse()
            
    def get_contents(self):
        return self.file_contents
        
    def _iter_contents(self):
        if self.file_contents is None:
            return ValueError('No file contents in this object'+str(self))
        else:
            for i in self.file_contents: 
                # time, category
                yield (self.time_added, self.file_path, i.lstrip('http://').lstrip('www.').split('.')[0], i)












def get_data(fp):
    """ Get data from .txt files in a directory """
    import os
    files_list = os.listdir(fp)
    if len(files_list) < 1:
        print('No files exist! Exiting')
        exit()
    else:
        tree = FilesTree()
        for filename in os.listdir(fp):
            if '.txt' in filename:
                f = FileObject()
                tree.add(f.add(fp, filename))
        return tree
        
def redis_hash_load(tree):
    import redis
    r = redis.Redis(host='recent-sites-redis',port=6379)
    set_added, hash_added = 0,0
    for f in tree.__iter__:
        for time_added, filename, site_name, url in f._iter_contents:
            set_added += r.sadd(filename,url)
            redis_hash_dict = { 'time_added' : time_added , 'site_name' : site_name , 'notes' : '', 'priority' : 0 }
            hash_insert_result = r.hmset(url, redis_hash_dict )
            if hash_insert_result == "OK": hash_added +=1
    return idx, set_added, hash_added

def main(filepath = './app/data/'):
    parsed, set_added, hash_added = redis_hash_load(get_data(filepath))
    print(parsed,set_added,hash_added)

if __name__ == '__main__':
    main()
