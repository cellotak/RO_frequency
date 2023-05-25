#テキストデータを取り込み、各ROごとに平均値を出してファイル順に並べたCSVを生成するプログラム
import csv
import glob
import os
import re

#rawdataフォルダ内のデータのファイルパスをすべて取り込む
filesname = glob.glob("rawdata/*")

#既に処理済みデータがある場合は上書き
if os.path.exists('processed_data.csv'):
    os.remove('processed_data.csv')

#1ファイルごとに各ROの平均値を求めて出力ファイルに書き込む
for file in filesname:

    lines = [line.rstrip() for line in open(file)] 

    ro_frequencies=[[],[],[],[],[]]
    all_ro = []

    for i in range(1650,2070):
        ro_frequencies[0].append(int(lines[i]))
        
    for i in range(1230,1650):
        ro_frequencies[1].append(int(lines[i]))

    for i in range(810,1230):
        ro_frequencies[2].append(int(lines[i]))
        
    for i in range(390,810):
        ro_frequencies[3].append(int(lines[i]))
        
    for i in range(0,390):
        ro_frequencies[4].append(int(lines[i]))

    for ro_frequency in ro_frequencies:
        average = sum(ro_frequency)/len(ro_frequency)
        all_ro.append(average)
    
    with open('processed_data.csv','a',newline='') as f:
        writer = csv.writer(f)
        writer.writerow(all_ro)