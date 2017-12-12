#!/usr/bin/python

def get_data(fp):
	import os
	d, files_list = dict(), os.listdir(fp)
	if len(files_list) < 1:
		print('No files exist! Exiting')
		exit()
	else:
		for filename in os.listdir(fp):
			if '.txt' in filename:
				with open(fp + filename,'r') as f:
					l  = [ line.rstrip('\n\r') for line in f.readlines() ]
				l.reverse()
				d[filename] = l
	return d

def redis_hash_load(d):
	import redis, datetime
	r = redis.Redis(host='recent-sites-redis',port=6379)
	set_added, hash_added = 0,0
	for idx, items in enumerate(d.items()):
		filename, urls = items
		for url in urls:
			time_added = datetime.datetime.now().strftime('%H:%M-%m/%d/%Y')
			site_name = url.lstrip('http://').lstrip('www.').split('.')[0]
			set_added += r.sadd(filename,url)
			hash_insert_result = r.hmset(url, { 'time_added' : time_added , 'site_name' : site_name , 'notes' : '', 'priority' : 0 } )
			if hash_insert_result == "OK":
				hash_added +=1
	return idx, set_added, hash_added

def main(filepath = '/home/data/'):
	parsed, set_added, hash_added = redis_hash_load(get_data(filepath))
	print(parsed,set_added,hash_added)

if __name__ == '__main__':
	main()
