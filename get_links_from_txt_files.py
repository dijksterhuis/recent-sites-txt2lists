def get_data(filepath='/home/ec2-user/'):
	import os
	d, files_list = dict(), os.listdir(filepath)
	if len(files_list) < 1:
		print('No files exist! Exiting')
		exit()
	else:
		for filename in os.listdir(filepath):
			if '.txt' in filename:
				with open(filepath + filename,'r') as f:
					l  = [ line.rstrip('\n\r') for line in f.readlines() ]
				l.reverse()
				d[filename] = l
	return d

