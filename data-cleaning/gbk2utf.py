##############################
#   Written By lsvih         #
#   2017-04-06               #
#   gbk to utf-8             #
##############################
# -*- coding:utf-8 -*-
#encoding:utf-8
import os
import codecs

def ReadFile(filePath,encoding="gbk"):
    with codecs.open(filePath,"r",encoding) as f:
        return f.read()

def WriteFile(filePath,u,encoding="utf-8"):
    with codecs.open(filePath,"w",encoding) as f:
        f.write(u)

def GBK2UTF8(src,dst):
    content = ReadFile(src,encoding="gbk")
    WriteFile(dst,content,encoding="utf-8")

def ListFiles(data_folder):
    for i in os.listdir(data_folder):
        if i.endswith('.csv'):
            GBK2UTF8(i,i[:-4]+'_utf.csv')

def main():
    ListFiles('./')

if __name__=='__main__':
    main()
