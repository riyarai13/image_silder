"""import modules tkinter creates application window ,provides functions to develop gui 
cycle provides an iterator object to iterate through lists of images """
import tkinter as tk
from itertools import cycle
from PIL import ImageTk, Image

"""main class it creates the window"""


class App(tk.Tk):

    def __init__(self, imagelist, x, y, delaytime):
        tk.Tk.__init__(self)
        # geometry defines the dimension of our slider's window x refers to how much winow will move along x axis
        # and y refers to how much window will move aliong y axis

        self.geometry('700x700')
        self.delay = delaytime
        #cycle iterate in the images list 
        #to read the image we have imported the pil module
        #image = image.resize((450, 350), Image.ANTIALIAS)
        self.pict_iterator = cycle((ImageTk.PhotoImage((Image.open(image)).resize((300,300),Image.ANTIALIAS)), image) for image in imagelist)
        #ths object is the main widget that is label in which our picture will be displayed
        self.displayobject = tk.Label(self,bg='pink')
        #pack is a attricute of label 
        self.displayobject.pack(expand="True",fill="both")

    """main function in which our image is displayed in the label """
    def display_images(self):
        #this is the image object and the name of the image
        curr_img, img_name = next(self.pict_iterator)
        #changing the content of our label. ie, including image in the label
        self.displayobject.config(image=curr_img)
        #displaying image name in place of title of our window
        self.title = img_name
        #after function for every widget,this is the infinte recursion
        self.after(self.delay, self.display_images)

    def run(self):
        """this is our main function through which gui will get activated"""
        self.mainloop()


imagelist = ['7.gif','1.gif','2.gif','3.gif','4.gif','5.gif']

# s.unsplash.com/photo-1590845947379-6c663322efea?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1534&q=80']
delaytime = 1000
x = 800
y = 367
mainobj = App(imagelist, x, y, delaytime)
mainobj.display_images()
mainobj.run()
