import cv2

# تحميل موديل مدرب مسبقاً (سأعطيكِ الطريقة لجلب الملفات بالأسفل)
# هذا مثال لكود يستخدم خوارزمية ذكية لكشف العناصر
def detect_objects(img_path):
    # قراءة الصورة
    image = cv2.imread(img_path)
    if image is None:
        print("الصورة غير موجودة!")
        return

    # تحويل الصورة إلى "أبيض وأسود" بشكل احترافي أو تطبيق فلتر ذكي
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # استخدام كاشف الوجوه (Face Detection) كمثال أولي احترافي
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # رسم مربعات حول الوجوه المكتشفة
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 3)
        cv2.putText(image, 'Human Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

    # عرض النتيجة
    cv2.imshow('AI Detection', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# تشغيل البرنامج على صورة البنت الموجودة في مشروعك
detect_objects('test.jpg'
