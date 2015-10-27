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

from Tkinter import *
 root = Tk()

 w = Label(root, text= "Here's your diary")
 w.pack()

root.mainloop()
 
 def open():
     print txt.read()

 def save():
     txt.close

 def add():
      
	 

 menubar = Menu(root)

 filemenu = Menu(menubar,tearoff=0)
 filemenu.add_command(label = "Add", command = open)
 filemenu.add_command(label = "Save", command = save)
 filemenu.add_separator()
 filemenu.add_command(label = "Exit", command = root.quit)
 menubar.add_cascade(label = "File", menu = filemenu)

 editmenu = Menu(menubar, tearoff=0)
 editmenu.add_command(label="Cut", command=hello)
 editmenu.add_command(label="Copy", command=hello)
 editmenu.add_command(label="Paste", command=hello)
 menubar.add_cascade(label="Edit",menu=editmenu)

 helpmenu = Menu(menubar, tearoff=0)
 helpmenu.add_command(label="About", command=about)
 menubar.add_cascade(label="Help", menu=helpmenu)

 root.config(menu=menubar)

 mainloop()
  

