import cv2
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
image = cv2.imread('pic/test1.png')
text = pytesseract.image_to_string(image, lang='kor+eng')
print('Texto: ', text)

cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()