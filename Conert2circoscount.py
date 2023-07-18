# _*_ coding: utf-8 _*_
"""
Created on 2023/7/18 20:56

@author: Wangpf

@Email: 206462763@qq.com
"""
import sys
#每条染色体的长度

chr1 = [0, 158534110]
chr2 = [0, 136231102]
chr3 = [0, 121005158]
chr4 = [0, 120000601]
chr5 = [0, 120089316]
chr6 = [0, 117806340]
chr7 = [0, 110682743]
chr8 = [0, 113319770]
chr9 = [0, 105454467]
chr10 = [0, 103308737]
chr11 = [0, 106982474]
chr12 = [0, 87216183]
chr13 = [0, 83472345]
chr14 = [0, 82403003]
chr15 = [0, 85007780]
chr16 = [0, 81013979]
chr17 = [0, 73167244]
chr18 = [0, 65820629]
chr19 = [0, 63449741]
chr20 = [0, 71974595]
chr21 = [0, 69862954]
chr22 = [0, 60773035]
chr23 = [0, 52498615]
chr24 = [0, 62317253]
chr25 = [0, 42350435]
chr26 = [0, 51992305]
chr27 = [0, 45612108]
chr28 = [0, 45940150]
chr29 = [0, 51098607]



step = sys.argv[2]  # 5mb
step = float(step)*1000000

winumber = chr1[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr1[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 2:
                    if int(line[0])==1 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(1, start, end, a[-1])
    except:
        pass

winumber = chr2[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr2[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 3:
                    if int(line[0])==2 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(2, start, end, a[-1])
    except:
        pass

winumber = chr3[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr3[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 4:
                    if int(line[0])==3 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(3, start, end, a[-1])
    except:
        pass

winumber = chr4[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr4[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 5:
                    if int(line[0])==4 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(4, start, end, a[-1])
    except:
        pass

winumber = chr5[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr5[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 6:
                    if int(line[0])==5 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(5, start, end, a[-1])
    except:
        pass

winumber = chr6[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr6[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 7:
                    if int(line[0])==6 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(6, start, end, a[-1])
    except:
        pass

winumber = chr7[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr7[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 8:
                    if int(line[0])==7 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(7, start, end, a[-1])
    except:
        pass

winumber = chr8[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr8[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 9:
                    if int(line[0])==8 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(8, start, end, a[-1])
    except:
        pass

winumber = chr9[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr9[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 10:
                    if int(line[0])==9 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(9, start, end, a[-1])
    except:
        pass

winumber = chr10[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr10[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 11:
                    if int(line[0])==10 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(10, start, end, a[-1])
    except:
        pass

winumber = chr11[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr11[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 12:
                    if int(line[0])==11 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(11, start, end, a[-1])
    except:
        pass

winumber = chr12[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr12[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 13:
                    if int(line[0])==12 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(12, start, end, a[-1])
    except:
        pass

winumber = chr13[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr13[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 14:
                    if int(line[0])==13 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(13, start, end, a[-1])
    except:
        pass

winumber = chr14[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr14[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 15:
                    if int(line[0])==14 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(14, start, end, a[-1])
    except:
        pass

winumber = chr15[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr15[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 16:
                    if int(line[0])==15 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(15, start, end, a[-1])
    except:
        pass

winumber = chr16[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr16[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 17:
                    if int(line[0])==16 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(16, start, end, a[-1])
    except:
        pass

winumber = chr17[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr17[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 18:
                    if int(line[0])==17 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(17, start, end, a[-1])
    except:
        pass

winumber = chr18[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr18[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 19:
                    if int(line[0])==18 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(18, start, end, a[-1])
    except:
        pass

winumber = chr19[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr19[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 20:
                    if int(line[0])==19 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(19, start, end, a[-1])
    except:
        pass

winumber = chr20[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr20[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 21:
                    if int(line[0])==20 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(20, start, end, a[-1])
    except:
        pass

winumber = chr21[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr21[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 22:
                    if int(line[0])==21 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(21, start, end, a[-1])
    except:
        pass

winumber = chr22[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr22[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 23:
                    if int(line[0])==22 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(22, start, end, a[-1])
    except:
        pass

winumber = chr23[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr23[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 24:
                    if int(line[0])==23 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(23, start, end, a[-1])
    except:
        pass

winumber = chr24[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr24[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 25:
                    if int(line[0])==24 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(24, start, end, a[-1])
    except:
        pass

winumber = chr25[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr25[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 26:
                    if int(line[0])==25 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(25, start, end, a[-1])
    except:
        pass

winumber = chr26[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr26[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 27:
                    if int(line[0])==26 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(26, start, end, a[-1])
    except:
        pass

winumber = chr27[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr27[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 28:
                    if int(line[0])==27 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(27, start, end, a[-1])
    except:
        pass

winumber = chr28[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr28[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 29:
                    if int(line[0])==28 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(28, start, end, a[-1])
    except:
        pass

winumber = chr29[1] // step + 1
for i in range(winumber):
    start = 0 + i * step
    end = step + i * step
    if i == winumber - 1:
        end = chr29[1]
    fo = open(sys.argv[1], "r")
    count = 0
    a = []
    try:
        for line in fo:
            if line.startswith("#"):
                pass
            else:
                line = line.strip().split()
                if int(line[0]) < 30:
                    if int(line[0])==29 and int(line[1]) > int(start) and int(line[2]) < int(end):
                        count = count + 1
                        a.append(count)
                else:
                    break
        print(29, start, end, a[-1])
    except:
        pass

