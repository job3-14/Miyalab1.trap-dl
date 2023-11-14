#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
画像を読み込み白黒に変換するプログラム
./input直下入力された画像をモノクロに変換し./outputに保存します
"""

import cv2
import numpy as np
import sys
import os
import glob

output = 'output'
input = 'input'

def conversion(path, output_path):
    """
    画像を白黒に変換し保存します
    """
    im = cv2.imread(path)
    im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(output_path, im_gray)

def conv_processing(file_list):
    """
    ファイルリストから変換関数を繰り返します
    """
    count = 0
    for tmp_file in file_list:
        output_img_path = join_path('output',str(count)+'.jpg')
        count += 1
        conversion(tmp_file, output_img_path)


def join_path(*a_tuple):
    """
    ファイルをのディレクトリを返す。
    """
    return os.path.join(*a_tuple)

def make_directories(path):
    """
    出力するディレクトリを作成する
    """
    os.makedirs(path, exist_ok=True)

def open_file_list(input_path):
    """
    引数に指定されたファイルないのファイル名の配列を返す。
    input_path:　入力ディレクトリ
    """
    file_path = [] # フォルダ一覧

    path = os.path.join(input_path, '*')
    for j in glob.iglob(path):
        file_path.append(j)
    return file_path


def main():
    """
    メインプログラム
    常に0を応答
    """
    input = join_path('input')

    file_list = open_file_list(input) # 画像一覧を取得
    make_directories(output) # 出力用フォルダを作成
    conv_processing(file_list)


    return 0


if __name__ == '__main__':
    sys.exit(main())