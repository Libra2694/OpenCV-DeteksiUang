import cv2
import numpy as np

def detect_nominal(hsv_img):
    # --- Rp100.000 (Merah keunguan) ---
    lower_red = np.array([150, 80, 80])
    upper_red = np.array([180, 255, 255])
    mask_red = cv2.inRange(hsv_img, lower_red, upper_red)
    
    # --- Rp50.000 (Biru) ---
    lower_blue = np.array([90, 100, 100])
    upper_blue = np.array([130, 255, 255])
    mask_blue = cv2.inRange(hsv_img, lower_blue, upper_blue)

    # --- Rp20.000 (Hijau) ---
    lower_green = np.array([40, 50, 50])
    upper_green = np.array([80, 255, 255])
    mask_green = cv2.inRange(hsv_img, lower_green, upper_green)

    # --- Rp10.000 (Ungu keabu-abuan) ---
    lower_purple = np.array([130, 50, 50])
    upper_purple = np.array([145, 255, 255])
    mask_purple = cv2.inRange(hsv_img, lower_purple, upper_purple)

    # Hitung luas setiap warna
    count_red = cv2.countNonZero(mask_red)
    count_blue = cv2.countNonZero(mask_blue)
    count_green = cv2.countNonZero(mask_green)
    count_purple = cv2.countNonZero(mask_purple)

    # Threshold kasar (bisa disesuaikan berdasarkan kualitas kamera/gambar)
    if count_red > 5000:
        return "Rp100.000"
    elif count_blue > 5000:
        return "Rp50.000"
    elif count_green > 5000:
        return "Rp20.000"
    elif count_purple > 5000:
        return "Rp10.000"

    return "Tidak dikenali"

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    nominal = detect_nominal(hsv)

    cv2.putText(frame, f"Uang: {nominal}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1, (0, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow("Deteksi Uang (Kamera)", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
