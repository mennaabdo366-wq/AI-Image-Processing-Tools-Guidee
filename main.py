import cv2

# قراءة الصورة
img = cv2.imread('test.jpg')

if img is not None:
    # تحويل لرمادي
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # كشف الحواف
    edges = cv2.Canny(gray, 100, 200)
    # حفظ النتيجة
    cv2.imwrite('output.jpg', edges)
    print("تمت المعالجة بنجاح!")
