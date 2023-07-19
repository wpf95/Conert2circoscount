# _*_ coding: utf-8 _*_
"""
Created on 2023/7/19 16:12

@author: Wangpf

@Email: 206462763@qq.com
"""

import  sys
# 1.setting the every chrom length you want to visual

chr1 = [0, 158534110]; chr2 = [0, 136231102];chr3 = [0, 121005158];chr4 = [0, 120000601];chr5 = [0, 120089316];chr6 = [0, 117806340]
chr7 = [0, 110682743];chr8 = [0, 113319770];chr9 = [0, 105454467];chr10 = [0, 103308737];chr11 = [0, 106982474];chr12 = [0, 87216183]
chr13 = [0, 83472345];chr14 = [0, 82403003];chr15 = [0, 85007780];chr16 = [0, 81013979];chr17 = [0, 73167244];chr18 = [0, 65820629]
chr19 = [0, 63449741];chr20 = [0, 71974595];chr21 = [0, 69862954];chr22 = [0, 60773035];chr23 = [0, 52498615];chr24 = [0, 62317253]
chr25 = [0, 42350435];chr26 = [0, 51992305];chr27 = [0, 45612108];chr28 = [0, 45940150];chr29 = [0, 51098607]
chrX = [0, 139009144]
#chrY = [0, XXXX]  chrZ = [0, XXXX] chrW = [0, XXXX]

X = 'X';Y='Y';Z = 'Z';W='W'
x = 'X';y='Y';z = 'Z';w='W'

def judge(x):
    if x==101:
        return 'X'
    elif x==102:
        return 'Y'
    elif x==103:
        return 'Z'
    elif x==104:
        return 'W'
    else:
        return x
        
#2.setting your bins unit is Mb
step = sys.argv[2]  # 5mb
step = int(float(step)*1000000)
# step=5000000

def convet(chrom, num):
    if num == 'X':
        num = 101
    elif num == 'Y':
        num = 102
    elif num == 'Z':
        num = 103
    elif num == 'W':
        num = 104

    winumber = chrom[1] // step + 1

    for i in range(winumber):
        start = 0 + i * step
        end = step + i * step
        if i == winumber - 1:
            end = chrom[1]
        fo = open(sys.argv[1], "r")
        count = 0
        a = []
        try:
            for line in fo:
                if line.startswith("#"):
                    pass
                else:
                    line = line.strip().split()
                    if line[0] == 'X' or line[0] == 'x':
                        line[0] = 101
                    elif line[0] == 'Y'or line[0] == 'y':
                        line[0] = 102
                    if line[0] == 'Z' or line[0] == 'z':
                        line[0] = 103
                    elif line[0] == 'W'or line[0] == 'w':
                        line[0] = 104
                    if int(line[0]) < num + 1:
                        if str(line[0]) == str(num) and int(line[1]) > int(start) and int(line[2]) < int(end):
                            count = count + 1
                            a.append(count)
                    else:
                        break
            print(judge(num), start, end, a[-1])
        except:
            pass

convet(chr1, 1), convet(chr2, 2), convet(chr3, 3), convet(chr4, 4), convet(chr5, 5), convet(chr6, 6),
convet(chr7,7), convet(chr8, 8), convet(chr9, 9), convet(chr10, 10), convet(chr11, 11), convet(chr12, 12), convet(chr13, 13),
convet(chr14,14), convet(chr15, 15), convet(chr16, 16), convet(chr17, 17), convet(chr18, 18), convet(chr19, 19), convet(chr20, 20),
convet(chr21, 21), convet(chr22, 22), convet(chr23, 23), convet(chr24, 24), convet(chr25, 25), convet(chr26, 26),
convet(chr27, 27), convet(chr28, 28), convet(chr29, 29)
#convet(chrX,X)



