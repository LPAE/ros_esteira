import cv2

capture = cv2.VideoCapture(2)

count_frame = 0
while 1:
    ret, frame = capture.read()
    cv2.imshow("Video", frame)
    cv2.imwrite(str(count_frame) + '_frame.png', frame)
    print(count_frame)
    count_frame += 1
    # ------------------------------------------------------------------------------------------------------------------
    # Esc -> EXIT while
    while 1:
      k = cv2.waitKey(1) & 0xff
      if k ==13 or k==27:
        break

    if k == 27:
        break
    # ------------------------------------------------------------------------------------------------------------------
capture.release()
cv2.destroyAllWindows()