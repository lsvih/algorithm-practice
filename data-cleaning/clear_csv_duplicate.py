##############################
#   Written By lsvih         #
#   2017-04-06               #
#   delete duplicate data    #
##############################
# -*- coding:utf-8 -*-
#encoding:utf-8
import os

MAX = 200
def importcsv(filename):
    print('cleaning ' + filename)
    rows,count = [],0#temp data
    g=file(filename[:-4] + '_clean.csv',"w+")
    with open(filename, 'r') as f:
        line = f.readline()
        while line:
            line = line.replace('\n','')
            line = line.replace('\r','')
            if line not in rows:
                rows.append(line)
                g.writelines(line)
                g.writelines('\n')
                if len(rows) >= MAX:rows = []
            else:
                count += 1
            line = f.readline()
    print(filename+' had cleaned '+ count + ' duplicate data.')
    g.close()

def ListFiles(data_folder):
    for i in os.listdir(data_folder):
        if i.endswith('.csv'):
            importcsv(i)

def main():
    ListFiles("./")

if __name__=='__main__':
    main()
