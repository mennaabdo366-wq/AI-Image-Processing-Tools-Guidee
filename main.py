import cv2

# 1. قراءة الصورة
image = cv2.imread(&#39;image_path.jpg&#39;) 

if image is not None:
    # 2. تحويل الصورة إلى اللون الرمادي
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 3. كشف الحواف باستخدام خوارزمية Canny
    edges = cv2.Canny(gray_image, 100, 200)
    
    # 4. حفظ النتيجة النهائية
    cv2.imwrite(&#39;output_edges.jpg&#39;, edges)
    print(&quot;تمت معالجة الصورة بنجاح!&quot;)
else:
    print(&quot;خطأ: تأكدي من اسم ملف الصورة المرفوع&quot;)
