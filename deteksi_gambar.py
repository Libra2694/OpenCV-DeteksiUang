import cv2
import numpy as np

def detect_nominal(hsv_img):
    nominal_dict = {
        "Rp100.000": ((150, 100, 100), (180, 255, 255)),
        "Rp50.000": ((90, 100, 100), (130, 255, 255)),
        "Rp20.000": ((40, 50, 50), (80, 255, 255)),
        "Rp10.000": ((130, 50, 50), (145, 255, 255)),
        "Rp5.000": ((20, 50, 50), (30, 255, 255)),     # Hypothetical HSV range
        "Rp2.000": ((10, 50, 50), (20, 255, 255)),    # Hypothetical HSV range
        "Rp1.000": ((0, 50, 50), (10, 255, 255))      # Hypothetical HSV range
    }

    for nominal, (lower, upper) in nominal_dict.items():
        mask = cv2.inRange(hsv_img, lower, upper)
        if cv2.countNonZero(mask) > 5000:
            return nominal

    return "Tidak dikenali"

# Ganti path ke gambar uang kamu
img = cv2.imread('image/100000.png') # ganti file foto uang nya disini  
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

nominal = detect_nominal(hsv)

# Tampilkan hasil
cv2.putText(img, f"Nominal: {nominal}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 
            1, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow("Deteksi Uang (Foto)", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

