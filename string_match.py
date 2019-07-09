import re
str1='ATTUGTCUATUUGATTGCAUGTCCGCUAUTCAGATTUGTCGUUTTAUGTCCGG'
def string_match(str,start,ending):
    STORGE=[]
    for i in range(0,len(str1)-6):
        if str1[i]==start:
            if  str1[i+6]==ending:
                print(str1[i-1:i+8:1])
                s=str1[i-1:i+8:1]
                STORGE.append(s)
            else:
                pass

        else:
                pass
        i=i+1
    print("满足您的条件的多肽一共有%d个，他们是："%(len(STORGE)),STORGE)
    return STORGE

start=input("请输入开始的碱基")
ending=input("请输入结束的碱基")
string_match(str1,start,ending)