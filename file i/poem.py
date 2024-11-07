f = open("/Users/sonu/Documents/python/file i/p/poem.txt")
content = f.read()
if("twinkle" in content):
    print("present")
else:
    print("not present")
f.close()        