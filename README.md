# AI-Image-Processing-Tools-Guidee
#![my Test Image](test.jpg)
#![my image_path Image](image_path.jpg)
import cv2

# قراءة الصورة التي قمتِ برفعها
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
    print("خطأ: لم يتم العثور على ملف الصورة. تأكدي من الاسم.")
