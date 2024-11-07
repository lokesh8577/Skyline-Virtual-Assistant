with open('/Users/sonu/Documents/python/file i/log.txt','r') as f:
    item = f.read()
    if('python' in item):
        print("python exist in log file")

    else:
        print("not exist in log file")     