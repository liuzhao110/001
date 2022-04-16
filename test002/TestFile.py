# coding = gbk
list1 = ['physics', 'chemistry', 1997, 2000]
with open("E://filename.txt", 'r',encoding="utf-8") as f:
    for line in f:
        if '"name"'  in line:
            for myLine in list1:
                myLine = myLine.strip()
                line = line.strip()
                if myLine == line:
                    print(line, end='')
            list1.append(line)