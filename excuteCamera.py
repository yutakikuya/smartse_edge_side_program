# coding: utf-8
#!/usr/bin/env python
import cv2
import datetime
import os
import numpy as np
import pytz

def isCapturable(l):
	#暗かったら撮影しない
	return l > 30

#画像出力フォルダ
room_img_folder = "./room/"

now=datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
#日付フォルダ作成処理
if not os.path.exists(room_img_folder+"{0:%Y%m%d}".format(now)):
	os.makedirs(room_img_folder+"{0:%Y%m%d}".format(now))

#撮影処理
cap = cv2.VideoCapture(0)

ret, frame = cap.read()
frame_avg = np.average(frame)
print(frame_avg)
if isCapturable(frame_avg):
	now_str="{0:%Y%m%d-%H%M}".format(now)
	cv2.imwrite(room_img_folder+"{0:%Y%m%d}".format(now)+"/"+now_str+".jpg",frame)

cap.release()
cv2.destroyAllWindows()
