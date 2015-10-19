import time

timeStamp = int(time.time()) 
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)

print "How are you today?" 
content = raw_input(">")

txt = open('Dairy.txt', 'a+')

txt.write(otherStyleTime)
txt.write("\n")
txt.write(content)
txt.write("\n")

text.close 

print "Here's your dairy:"
print txt.read()
