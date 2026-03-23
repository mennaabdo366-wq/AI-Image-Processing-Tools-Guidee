# 📸 AI Image Processing Tools Guide

هذا المشروع يوضح خطوات معالجة الصور الرقمية باستخدام مكتبة OpenCV.

### 🖼️ نماذج من المعالجة
![Test Image](test.jpg)
![Image Path Result](image_path.jpg)

### 💻 كود المعالجة (Python Code)
```python
import cv2

# قراءة الصورة
image = cv2.imread('image_path.jpg')

if image is not None:
    # 1. تحويل الصورة إلى اللون الرمادي
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 2. كشف الحواف باستخدام خوارزمية Canny
    edges = cv2.Canny(gray_image, 100, 200)
    
    # حفظ النتيجة النهائية
    cv2.imwrite('output_edges.jpg', edges)
    print("تمت معالجة الصورة بنجاح!")
else:
    print("خطأ: تأكدي من اسم ملف الصورة المرفوع")
