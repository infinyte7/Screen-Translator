# Screen-Translator
Using snip to take screenshot after that Take OCR of the Image, then translate text.

## Library used in this project
```
pytesseract
tkinter
PIL
PyQt5
```

## Install Tesseract-OCR then import pytesseract 
```python
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
self.text = pytesseract.image_to_string(Image.open('Capture.jpg'), lang=self.lang)
```

## Using ScreenCapture.py in main.py to select screenshot area on screen
```python
import subprocess 

subprocess.call(['python', 'ScreenCapture.py'], shell=True)
```
### Save the file with .pyw extension to hide console
```
main.py  -->   main.pyw
ScreenCapture.py  -->  ScreenCapture.py
```

![alt text](https://github.com/infinyte7/Screen-Translator/blob/master/screenshot.png)
