
"""
    编写一个程序，从终端输入一个单词，打印出该单词的解释，
    如果输入的单词找不到则打印 “没有该单词”
"""
fo = open("words.txt")
fw = input("请输入单词:")
for line in fo:
    re = line.split(' ',1)[0]
    if re > fw:
        print("没有该单词")
        break
    elif re == fw:
        print(line)
        break
else:
    print("没有该单词")
