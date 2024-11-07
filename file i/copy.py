with open('/Users/sonu/Documents/python/file i/this.txt','r') as f:
    content=f.read()

with open("/Users/sonu/Documents/python/file i/this_copy.txt",'w') as f:
    f.write(content)
    
