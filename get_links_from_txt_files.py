def get_data(filepath='/home/ec2-user/'):
    import os
    d, files_list = dict(), os.listdir(filepath)
    if len(files_list) < 1:
        print('No files exist! Exiting')
        exit()
    else:
        for filename in os.listdir(filepath):
            print('FILENAME:', filename)
            if '.txt' in filename:
                l = list()
                with open(filepath + filename,'r') as f:
                    for line in f.readlines():
                        try: l.append(line.rstrip('\n\r'))
                        except UnicodeDecodeError: l.append("ERROR LOADING: "+str(line))
                l.reverse()
                d[filename] = l
    return d

