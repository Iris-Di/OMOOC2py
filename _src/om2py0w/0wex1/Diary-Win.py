import time

timeStamp = int(time.time()) 
timeArray = time.localtime(timeStamp)
otherStyleTime = time.strftime("%Y/%m/%d %H:%M:%S", timeArray)


txt = open('Diary.txt', 'a+')

print "Here's your diary:"
print txt.read()

txt.close

txt = open('Diary.txt', 'a')

print "How are you today? (Enter quit to finish writing)" 

while True:
    content = raw_input('Write down something you want to remember: ')
    if content == 'quit':
	     break
		 
    txt.write(otherStyleTime)
    txt.write("\n")
    txt.write(content)
    txt.write("\n")

txt.close

    

