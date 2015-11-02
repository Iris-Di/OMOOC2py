from Tkinter import *

class Application(Frame):
    def diary(self):
	    print "Here is your diary:"
		
		def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "QUIT"
		self.QUIT["command"] = self.quit
		
		self.QUIT.pack({"side":"left"})
		
		self.PRINT = Button(self)
		self.PRINT["text"] = "Print"
		self.PRINT["command"] = self.diary
		
		self.PRINT.pack({"side":"left"})
		
	def __init__(self, master=None):
	    Frame.__init__(self, master)
		self.pack()
		self.createWidgets()
		
	root = Tk()
	app =Application(master=root)
	app.mainloop()
	root.destroy()
		
		