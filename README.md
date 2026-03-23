# 📸 AI Image Processing Project
مشروع معالجة الصور الرقمية - جامعة دمياط

## 🖼️ نماذج الصور المرفوعة
![الصورة الأولى](test.jpg)
![الصورة الثانية](image_path.jpg)

## 💻 كود المعالجة (Python)
```python
import cv2

# قراءة الصورة
image = cv2.imread('image_path.jpg')

if image is not None:
    # تحويل للرمادي وكشف الحواف
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    cv2.imwrite('output.jpg', edges)
    print("Success!")
