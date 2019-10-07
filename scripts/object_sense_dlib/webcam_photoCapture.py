import cv2

capture = cv2.VideoCapture(2)

count_frame = 0
while 1:
    ret, frame = capture.read()
    cv2.imshow("Video", frame)

    # ------------------------------------------------------------------------------------------------------------------
    # Esc -> EXIT while
    while 1:
      k = cv2.waitKey(1) & 0xff
      if k==13 or k==ord('p') or k==ord('t'):
        break
    
    if k==ord('t'):
        cv2.imwrite(str(count_frame) + '_frame.png', frame)
        print(count_frame)
        count_frame += 1

    if k == 27:
        break
    # -----------------------------------t-------------------------------------------------------------------------------
capture.release()
cv2.destroyAllWindows()