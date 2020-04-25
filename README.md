# Screen-Translator
Using snip to take screenshot after that Take OCR of the Image, then translate text.

# Library used in this project
```
pytesseract
tkinter
PIL
PyQt5
```

# Using Tesseract-OCR
```python
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
self.text = pytesseract.image_to_string(Image.open('Capture.jpg'), lang=self.lang)
```

# Using ScreenCapture.py
```python
import subprocess 

subprocess.call(['python', 'ScreenCapture.py'], shell=True)
```
# [Need to optimize and improve]

![alt text](https://github.com/infinyte7/Screen-Translator/blob/master/program_flow.png)
