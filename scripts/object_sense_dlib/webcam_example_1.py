import cv2

capture = cv2.VideoCapture(2)

while 1:
    ret, frame = capture.read()
    cv2.imshow("Video", frame)

    # ------------------------------------------------------------------------------------------------------------------
    # Esc -> EXIT while
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    # ------------------------------------------------------------------------------------------------------------------

capture.release()
cv2.destroyAllWindows()
