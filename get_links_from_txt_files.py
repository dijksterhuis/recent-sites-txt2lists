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
                    try:
                        l = [line.rstrip('\n\r') for line in f.readlines()]
                    except UnicodeDecodeError as e:
                        l = ["ERROR LOADING LINKS FROM FILE: "+str(e)]
                l.reverse()
                d[filename] = l
    return d

