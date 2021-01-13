import cv2
import time
cap = cv2.VideoCapture(6)
starting_time = time.time()
frame_id = 0
font = cv2.FONT_HERSHEY_SIMPLEX
while True:

    ret, frame = cap.read()
    elapsed_time = time.time() - starting_time
    fps = frame_id / elapsed_time
    cv2.putText(frame, "FPS: " + str(round(fps, 2)), (10, 50), font, 2, (0, 0, 0), 3)
    cv2.imshow('frame', frame)
    frame_id += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

