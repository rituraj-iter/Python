import cv2
import time
import pandas
from datetime import datetime
starting_frame = None
motion_status_list = [None, None]
time = []
data_frame = pandas.DataFrame(columns=["Start", "End"])
video = cv2.VideoCapture(0)
while True:
    check, frame = video.read()
    motion_status = 0
    gray_scale_image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_scale_image = cv2.GaussianBlur(gray_scale_image, (21, 21), 0)
    if starting_frame is None:
        starting_frame = gray_scale_image
        continue
    change_time_frame = cv2.absdiff(starting_frame, gray_scale_image)
    threshold_frame = cv2.threshold(
        change_time_frame, 30, 255, cv2.THRESH_BINARY)[1]
    threshold_frame = cv2.dilate(threshold_frame, None, iterations=2)
    moving_obj_countour, _ = cv2.findContours(
        threshold_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in moving_obj_countour:
        if cv2.contourArea(contour) < 10000:
            continue
        motion_status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)
    motion_status_list.append(motion_status)
    motion_status_list = motion_status_list[-2:]
    if motion_status_list[-1] == 1 and motion_status_list[-2] == 0:
        time.append(datetime.now())
    if motion_status_list[-1] == 0 and motion_status_list[-2] == 1:
        time.append(datetime.now())
    cv2.imshow("Gray Scale Frame", gray_scale_image)
    cv2.imshow("Frame Changer", change_time_frame)
    cv2.imshow("Black and white Frame", threshold_frame)
    cv2.imshow("Color Frame", frame)
    exit_key = cv2.waitKey(1)
    if exit_key == ord('e'):
        if motion_status == 1:
            time.append(datetime.now())
        break
for i in range(0, len(time), 2):
    data_frame = data_frame.append(
        {"Start": time[i], "End": time[i + 1]}, ignore_index=True)
data_frame.to_csv("movementstimes.csv")
video.release()
cv2.destroyAllWindows()
