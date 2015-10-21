import time

timeStamp = int(time.time()) 
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)

txt = open('Diary.txt')
print "Here's your diary:"
print txt.read()

txt = open('Diary.txt', 'a+')
print "How are you today?" 
content = raw_input(">")

txt.write(otherStyleTime)
txt.write("\n")
txt.write(content)
txt.write("\n")

txt.close