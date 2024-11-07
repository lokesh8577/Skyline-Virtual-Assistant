words =['donkey','Benny']
with open('/Users/sonu/Documents/python/file i/p/donkey.txt','r') as f:
    content=f.read()
for word in words:
    content=content.replace(word,"######")


with open("/Users/sonu/Documents/python/file i/p/donkey.txt",'w') as f:
    f.write(content)
