# coding: utf-8
import cv2
import os

def existFiles(path_to_file):
    file_list = sorted(os.listdir(img_folder+"/"+latest_directory),reverse=True)
    return len(file_list) > 0

def excuteScoringRoom(diff_img):
    #TODO
    return 1;

def filteringProcess(imgs):
    #TODO
    return filterd_img

#きれいな部屋画像（本気で作るならユーザが模様替えしたらアプリから変更できるようにすべき）
clean_room_img = cv2.imread("clean_room.jpg",0)
 
img_folder = "/home/pi/room/"
#todo: 10枚直近の画像取得
#for

#新しい画像を取得(作りは良くないが、roomフォルダ下に20200613のようなフォルダができている。その最新のフォルダを取得)
latest_directory = sorted(os.listdir(img_folder),reverse=True)[0]
print(latest_directory)
#背景差分で一日のきれい度を評価（直近１０枚の画像で評価）
if existFiles(img_folder+"/"+latest_directory):
    #TODO まだ実装してない
    latest_img_name = sorted(os.listdir(img_folder+"/"+latest_directory),reverse=True)[0]
    print(latest_img_name)
    #評価画像
    eval_img = cv2.imread(img_folder+"/"+latest_directory+"/"+latest_img_name,0)

    mask = cv2.absdiff(clean_room_img, eval_img)

    #画面に表示
    #cv2.imshow('frame', fgmask)
 
    #「差分」画像のファイル名

    #diff 10枚くらい
    bg_diff_path = "./diff3_3c.jpg"
 
    #「差分」画像の保存
    cv2.imwrite(bg_diff_path, mask)