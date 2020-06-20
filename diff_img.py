# coding: utf-8
import cv2
import os
import numpy as np
import os
import datetime
import pytz
import csv

def existFiles(path_to_file):
    file_list = sorted(os.listdir(img_folder+"/"+latest_directory),reverse=True)
    return len(file_list) > 0

#FIXME:機械学習等を使ってもっと汎用的に処理できるようにできる余地あり
def excuteScoringRoom(diff_img,mask_img):
    jedge_pixel_count = 0.
    dirty_pixel_count = 0.
    for x in range(diff_img.shape[0]):
        for y in range(diff_img.shape[1]):
            #ピクセルを取得
            #FIXME:カメラからはなられいる場所の空間領域が小さく評価される。修正余地あり
            if(mask_img[x][y] == 0):
                thes = 15#きれいな部屋のピクセルから何らかの変化があったピクセルを判断するための閾値
                jedge_pixel_count = jedge_pixel_count + 1
                val = diff_img[x][y]
                if  val > thes:
                    dirty_pixel_count += 1

    return dirty_pixel_count/jedge_pixel_count

#FIXME: きれいな部屋画像（本気で作るならユーザが模様替えしたらアプリから変更できるようにすべき）
clean_room_img = cv2.imread("clean_room.jpg",0)
#評価領域のマスク
mask_img = cv2.imread("mask.jpg",0)
 
eval_time ="2000"
img_folder = "./room/"

#新しい画像を取得(作りは良くないが、roomフォルダ下に20200613のようなフォルダができている。その最新のフォルダを取得)
latest_directory = sorted(os.listdir(img_folder),reverse=True)[0]


print(latest_directory)
#背景差分で一日のきれい度を評価
if existFiles(img_folder+"/"+latest_directory):
    #評価画像
    print(img_folder+latest_directory+"/"+latest_directory + eval_time + ".jpg")
    today_eval_img = cv2.imread(img_folder+latest_directory+"/"+latest_directory + eval_time + ".jpg",0)
    today_diff = cv2.absdiff(clean_room_img, today_eval_img)
    eval_val = excuteScoringRoom(today_diff,mask_img)
    #日付取得
    now=datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
    #csvに評価を追記
    with open('data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(["{0:%Y/%m/%d %H:%m:%S}".format(now),eval_val])
    print()

    #フォルダ生成
    diff_img_folder = "./diff/"
    
    if not os.path.exists(diff_img_folder+"{0:%Y%m%d}".format(now)):
	    os.makedirs(diff_img_folder+"{0:%Y%m%d}".format(now))
    #「差分」画像の保存
    cv2.imwrite(diff_img_folder+"{0:%Y%m%d}".format(now)+"/"+latest_directory + eval_time + "_diff.jpg", today_diff)
