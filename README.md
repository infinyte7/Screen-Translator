# Screen-Translator
Using snip to take screenshot after that Take OCR of the Image, then translate text.

## Quick Start
1. Install Python 
<br>https://www.python.org/downloads/

2. Install following python library using pip
```
pip install googletrans PyQt5 Pillow pytesseract
```

<br>3. Install Tesseract-OCR 
<br>https://tesseract-ocr.github.io/tessdoc/Downloads

<br>4. Ready to go

## Demo
![alt text](https://raw.githubusercontent.com/infinyte7/Screen-Translator/master/ScreenTranslate_demo.gif)

## Change installation directory of Tesseract-OCR in main.py
```python
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'  # Change to installation directory 
self.text = pytesseract.image_to_string(Image.open('Capture.jpg'), lang=self.lang_src)
```

## Adding other languages
<b>1.Install language data for Tesseract-OCR</b>
<b>2. Add option in</b>
```
.....
def changeLang(self):
        print("Change lang")

        SRC = [
        "Chinese",
        "English",
        "Hindi"  # <-- Added
        ] #etc
        .....
        .....
```
<b>3. Add following in ok()</b>
```
...
...
def ok():
            print ("value is:" + variable.get())
            print ("Target Lang.:" + dest_var.get())  
            
            # For hindi
            if "Hindi" in src_var.get():
                self.lang_src = "hin"
                print(self.lang_src)
.....
.....
```

<b>4. Add following to Translate(self)</b>
```
        if self.lang_dest == 'eng'and self.lang_src == "hin":
            tr = translator.translate(self.text, dest='en',src='hi')
            print(tr.text)
            self.textTrans = tr.text
        
        if self.lang_dest == 'chi_sim' and self.lang_src == "hin":
            tr = translator.translate(self.text, dest='zh-cn',src='hi')
            print(tr.text)
            self.textTrans = tr.text            
```

Language code for tesseract
<br>https://github.com/tesseract-ocr/tesseract/blob/master/doc/tesseract.1.asc#languages

<br>Language code for googletrans
<br>https://py-googletrans.readthedocs.io/en/latest/#googletrans-languages

<b>5. Ready to go</b>

### Save the file with .pyw extension to hide console
```
main.py  -->   main.pyw
ScreenCapture.py  -->  ScreenCapture.py
```

## License
<b>[Snipping-Tool](https://github.com/Rounak40/Snipping-Tool)</b>
<br>Rounak40
<br>MIT License 

<b>Screen Translate</b>
<br>Mani
<br>MIT License
