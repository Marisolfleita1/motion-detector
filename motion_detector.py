import cv2
import time
import datetime
import os

cap = cv2.VideoCapture(0)
time.sleep(2)

ret, frame1 = cap.read()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1_gray = cv2.GaussianBlur(frame1_gray, (21, 21), 0)

os.makedirs("capturas", exist_ok=True)

motion_detected = False
last_capture_time = 0
MIN_SECONDS_BETWEEN_CAPTURES = 10  # 5 minutos

# Inicializar detector de personas
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

while True:
    ret, frame2 = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    delta = cv2.absdiff(frame1_gray, gray)
    thresh = cv2.threshold(delta, 25, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    movement_now = False
    for c in contours:
        if cv2.contourArea(c) < 500:
            continue
        movement_now = True
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Detectar personas SOLO si hay movimiento
    persons, _ = hog.detectMultiScale(frame2, winStride=(8,8))
    
    # Dibujar rectángulos en personas detectadas
    for (x, y, w, h) in persons:
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame2, "Persona", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    # Guardar imagen solo si detecta movimiento Y al menos UNA persona
    current_time = time.time()
    if movement_now and len(persons) > 0 and not motion_detected:
        if current_time - last_capture_time > MIN_SECONDS_BETWEEN_CAPTURES:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            filename = f"capturas/mov_{timestamp}.jpg"
            cv2.imwrite(filename, frame2)
            print(f"📸 Captura guardada (persona detectada): {filename}")
            last_capture_time = current_time
        motion_detected = True

    if not movement_now:
        motion_detected = False

    cv2.imshow("Detector de Movimiento y Personas", frame2)
    key = cv2.waitKey(30) & 0xFF
    if key == ord("q"):
        break

    frame1_gray = gray

cap.release()
cv2.destroyAllWindows()
