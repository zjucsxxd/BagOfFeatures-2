#coding:utf-8
import codecs
import os
import os.path
import shutil

TARGET = "101_ObjectCategories"
OUTDIR = "caltech101"

# 出力ディレクトリがなければ作る
if not os.path.exists(OUTDIR):
    os.mkdir(OUTDIR)

for category in os.listdir(TARGET):
    for file in os.listdir("%s/%s" % (TARGET, category)):
        # 101_ObjectCategories/airplanes/image_0001.jpg
        image_file = "%s/%s/%s" % (TARGET, category, file)
        # caltech101/airplanes-0001.jpg
        rename_file = "%s/%s-%s" % (OUTDIR, category, file.replace("image_", ""))
        # ファイルをコピー
        print "%s -> %s" % (image_file, rename_file)
        shutil.copyfile(image_file, rename_file)
        