import cv2
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import matplotlib.pyplot as plt
from scipy import ndimage
from skimage import color, feature, io

def the_ultimate_vision_system(img_path):
    # --- 1. القراءة والتحضير (Pillow & OpenCV) ---
    img_cv = cv2.imread(img_path)
    img_pil = Image.open(img_path)
    gray_cv = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)

    # --- 2. كشف الوجوه الاحترافي (Haar Cascade) ---
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray_cv, 1.1, 4)
    img_faces = img_cv.copy()
    for (x, y, w, h) in faces:
        cv2.rectangle(img_faces, (x, y), (x+w, y+h), (0, 255, 255), 8) # برواز سماوي جذاب

    # --- 3. استخراج ملمس الصورة (Scikit-image LBP) ---
    # ميزة متقدمة جداً في كتابك لتحليل ملمس الجلد أو الأشياء
    lbp = feature.local_binary_pattern(gray_cv, P=8, R=1, method="uniform")

    # --- 4. مرشح غاوسي الرياضي (SciPy) ---
    scipy_blur = ndimage.gaussian_filter(gray_cv, sigma=3)

    # --- 5. العرض في لوحة تحكم احترافية (Matplotlib) ---
    plt.style.use('dark_background')
    fig = plt.figure(figsize=(16, 10))
    fig.suptitle('AI Master Vision System - University Level Project', fontsize=22, color='yellow')

    # عرض كشف الوجوه
    ax1 = plt.subplot(2, 3, 1)
    ax1.imshow(cv2.cvtColor(img_faces, cv2.COLOR_BGR2RGB))
    ax1.set_title('Face Recognition (OpenCV)', color='cyan')
    ax1.axis('off')

    # عرض تحليل الملمس (LBP)
    ax2 = plt.subplot(2, 3, 2)
    ax2.imshow(lbp, cmap='magma')
    ax2.set_title('Texture Extraction (Skimage)', color='cyan')
    ax2.axis('off')

    # عرض المرشح الرياضي (SciPy)
    ax3 = plt.subplot(2, 3, 3)
    ax3.imshow(scipy_blur, cmap='gray')
    ax3.set_title('Gaussian Math Filter (SciPy)', color='cyan')
    ax3.axis('off')

    # عرض تحسين الألوان (Pillow)
    enhanced_pil = ImageEnhance.Color(img_pil).enhance(2.0)
    ax4 = plt.subplot(2, 3, 4)
    ax4.imshow(enhanced_pil)
    ax4.set_title('Vivid Color Enhancement (Pillow)', color='cyan')
    ax4.axis('off')

    # عرض المدرج التكراري (Histogram)
    ax5 = plt.subplot(2, 3, (5, 6))
    ax5.hist(gray_cv.ravel(), bins=256, color='yellow', alpha=0.5)
    ax5.set_title('Global Pixel Distribution (Data Analysis)', color='yellow')
    ax5.set_facecolor('#111111')

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

# تشغيل المنصة
the_ultimate_vision_system('image_path.jpg')
