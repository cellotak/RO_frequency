#FPGAとマイコンの測定系によるSTOB1702のcsvデータを取り込んみ、各ROごとに平均値を出してファイル順に並べたCSVを生成するプログラム
import csv
import glob
import os
import re

#rowdataフォルダ内のデータのファイルパスをすべて取り込む
filesname = glob.glob("rawdata/*")

#既に処理済みデータがある場合は上書き
if os.path.exists('processed_data.csv'):
    os.remove('processed_data.csv')

#ファイルパスの.csvの直前数字の大きさで順番を並び替える
sorted_filesname=sorted(filesname, key=lambda s: int(re.search(r'(\d+)\.', s).groups()[0]))

#1ファイルごとに各ROの平均値を求めて出力ファイルに書き込む
for current_file in sorted_filesname:

    lines = [line.rstrip() for line in open(current_file)] 

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