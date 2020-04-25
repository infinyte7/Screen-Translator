from tkinter import *
from PIL import ImageTk, Image
import subprocess
import pytesseract
from googletrans import Translator
import time
class ScreenTranslate:

    def __init__(self, master):
        self.master = master
        master.title("Screen Translate")
        
        self.lang = "chi_sim"
        self.text = ""

        self.textTrans = ""

        self.capture = Button(master, text="Capture", command=self.capture)
        self.lang_button = Button(master, text="Language", command=self.changeLang)
        #self.btn = Button(master, text="Change Language", command=self.changeLang)

        # LAYOUT

        self.capture.grid(row=0, column=0,padx=(50, 10), pady=10)
        self.lang_button.grid(row=0, column=1,padx=(10, 50))
        #self.btn.grid(row=0, column=2)

    def capture(self):
        print("Capture")
        #print(self.lang)

        #open pyhton file for screenshot
        subprocess.call(['python', 'ScreenCapture.py'], shell=True)


        #create a new window to show image with translation
        imgApp = Toplevel()

        #get dimension of image
        imsize = Image.open('Capture.jpg')
        width, height = imsize.size

        #create window 
        wh = str(width+80) + 'x' + str(height+80)
        imgApp.geometry(wh)
        imgApp.title("Translation")
        imgApp.attributes('-topmost',True)

        menubar = Menu(imgApp)
        menubar.add_command(label="Translate",command=self.Translate)
        menubar.add_command(label="Language",command=self.changeLang)

        imgApp.config(menu=menubar)
        
        #canvas for showing image
        canvas = Canvas(imgApp, height=height, width=width)
        canvas.pack(padx=20,pady=20)
        
        #my_image = PhotoImage(file='Capture.jpg', master= mainApp)

        im = Image.open('Capture.jpg')
        canvas.image = ImageTk.PhotoImage(im)
        canvas.create_image(0, 0, image=canvas.image, anchor='nw')
        
        #canvas.create_image(0,0, anchor=NW, image=my_image)

        imgApp.mainloop()

        

    def changeLang(self):
        print("Change lang")

        OPTIONS = [
        "Chinese",
        "English"
        ] #etc

        master = Toplevel()
        variable = StringVar(master)
        variable.set(OPTIONS[0]) # default value
        master.attributes('-topmost',True)
        w = OptionMenu(master, variable, *OPTIONS)
        w.pack()

        def ok():
            print ("value is:" + variable.get())

            #self.lang="chi_sim"
            #print(self.lang)

            if "English" in variable.get():
                self.lang = "eng"
                print(self.lang)

            if "Chinese" in variable.get():
                self.lang = "chi_sim"
                print(self.lang)
                
            master.destroy()
            

        button = Button(master, text="OK", command=ok)
        button.pack()

        master.mainloop()

    def Translate(self):
        #tesseract library for image to OCR
        
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        self.text = pytesseract.image_to_string(Image.open('Capture.jpg'), lang=self.lang)

        #print OCR text to console
        print(self.text)

        #create a window for showing text from image  OCR
        OCRbox = Tk()
        OCRbox.geometry("515x620")
        OCRbox.title("Text")
        OCRbox.attributes('-topmost',True)

        #text box

        lbl = Label(OCRbox, text="Output")
        lbl.grid(column=0, row=0, padx=10)


        T = Text(OCRbox, wrap=WORD, width=70, height= 20)
        T.grid(column=0, row=1, padx=10, pady=10)
        T.tag_configure('tag-center', justify='center')

        if "chi_sim" in self.lang:
            opText = re.sub(r'(?<=[^\W\d_])\s+(?=[^\W\d_])', '', self.text)
            T.insert(END, opText)
        else:
            T.insert(END, self.text)
    

        translator = Translator()

        if self.lang == 'chi_sim':
            tr = translator.translate(self.text, dest='en',src='zh-cn')
            print(tr.text)
            self.textTrans = tr.text

            TransOut = Text(OCRbox, wrap=WORD, width=70, height= 20)
            TransOut.grid(column=0, row=3, padx=10, pady=10)
            TransOut.insert(END, self.textTrans)

        if self.lang == 'eng':
            tr = translator.translate(self.text, dest='zh-cn',src='en')
            print(tr.text)
            self.textTrans = tr.text

            TransOut = Text(OCRbox, wrap=WORD, width=70, height= 20)
            TransOut.grid(column=0, row=3, padx=10, pady=10)
            TransOut.insert(END, self.textTrans)
        
        OCRbox.mainloop()

root = Tk()
my_gui = ScreenTranslate(root)
root.mainloop()
