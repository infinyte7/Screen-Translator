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
        
        self.lang_src = "chi_sim"
        self.lang_dest = "eng"
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
        #print(self.lang_src)

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
        imgApp.title("Image")
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

        SRC = [
        "Chinese",
        "English",
        "Hindi"
        ] #etc

        DEST = [
        "Chinese",
        "English",
        "Hindi"
        ] #etc

        master = Toplevel()
        master.attributes('-topmost',True)
        
        lbl_lang_src = Label(master, text="Source Language")
        lbl_lang_src.grid(column=0, row=0, padx=10)
        
        src_var = StringVar(master)
        src_var.set(SRC[0]) # default value
        
        w1 = OptionMenu(master, src_var, *SRC)
        w1.grid(column=1,row=0,padx=10)

        dest_var = StringVar(master)
        dest_var.set(DEST[1]) # default value

        lbl_lang_dest = Label(master, text="Target Language")
        lbl_lang_dest.grid(column=0, row=1, padx=10)

        w2 = OptionMenu(master, dest_var, *DEST)
        w2.grid(column=1,row=1,padx=10)

        def ok():
            print ("Source Lang.:" + src_var.get())
            print ("Target Lang.:" + dest_var.get())            

            #self.lang="chi_sim"
            #print(self.lang_src)

            # Source Language Options
            if "English" in src_var.get():
                self.lang_src = "eng"
                print(self.lang_src)

            if "Chinese" in src_var.get():
                self.lang_src = "chi_sim"
                print(self.lang_src)

            if "Hindi" in src_var.get():
                self.lang_src = "hin"
                print(self.lang_src)

            
            # Target Language Option
            if "English" in dest_var.get():
                self.lang_dest = "eng"
                print(self.lang_dest)

            if "Chinese" in dest_var.get():
                self.lang_dest = "chi_sim"
                print(self.lang_dest)

            if "Hindi" in dest_var.get():
                self.lang_dest = "hin"
                print(self.lang_dest)
                
            master.destroy()
            

        button = Button(master, text="OK", command=ok)
        button.grid(column=0,row=2)

        master.mainloop()

    def Translate(self):
        #tesseract library for image to OCR
        
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
        self.text = pytesseract.image_to_string(Image.open('Capture.jpg'), lang=self.lang_src)

        #print OCR text to console
        print(self.text)

        #create a window for showing text from image  OCR
        OCRbox = Tk()
        OCRbox.geometry("515x620")
        OCRbox.title("Translation")
        OCRbox.attributes('-topmost',True)

        #text box

        lbl = Label(OCRbox, text="OCR Text")
        lbl.grid(column=0, row=0, padx=10)


        T = Text(OCRbox, wrap=WORD, width=70, height= 20)
        T.grid(column=0, row=1, padx=10, pady=10)
        T.tag_configure('tag-center', justify='center')

        
        T.insert(END, self.text)
    

        lbl_translate = Label(OCRbox, text="Translated")
        lbl_translate.grid(column=0, row=2, padx=10)

        translator = Translator()

        # Chinese to English, Hindi
        if self.lang_dest == 'chi_sim' and self.lang_src == "eng":
            tr = translator.translate(self.text, dest='zh-cn',src='en')
            print(tr.text)
            self.textTrans = tr.text
            
        if self.lang_dest == 'chi_sim' and self.lang_src == "hin":
            tr = translator.translate(self.text, dest='zh-cn',src='hi')
            print(tr.text)
            self.textTrans = tr.text

        
        if self.lang_dest == 'eng'and self.lang_src == "chi_sim":
            tr = translator.translate(self.text, dest='en',src='zh-cn')
            print(tr.text)
            self.textTrans = tr.text

        if self.lang_dest == 'eng'and self.lang_src == "hin":
            tr = translator.translate(self.text, dest='en',src='hi')
            print(tr.text)
            self.textTrans = tr.text

        
        if self.lang_dest == 'hin' and self.lang_src == "eng":
            tr = translator.translate(self.text, dest='hi',src='en')
            print(tr.text)
            self.textTrans = tr.text

        if self.lang_dest == 'hin' and self.lang_src == "chi_sim":
            tr = translator.translate(self.text, dest='hi',src='zh-cn')
            print(tr.text)
            self.textTrans = tr.text

               
        TransOut = Text(OCRbox, wrap=WORD, width=70, height= 20)
        TransOut.grid(column=0, row=3, padx=10, pady=10)
        TransOut.insert(END, self.textTrans)
        
        OCRbox.mainloop()

root = Tk()
my_gui = ScreenTranslate(root)
root.mainloop()
