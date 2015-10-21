import time

timeStamp = int(time.time()) 
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)

txt = open('Diary.txt', 'a+')
txt = open('Diary.txt', 'r+')

print "Here's your diary:"
print txt.read()
txt.close

print "How are you today?" 
content = raw_input(">")

txt.write(otherStyleTime)
txt.write("\n")
txt.write(content)
txt.write("\n")

txt.close
