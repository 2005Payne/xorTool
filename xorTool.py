def XC():
    list=[]
    a=int('0x'+input(),16)
    while(True):
        mode=input("숫자를 입력하세요(종료:exit):")
        if(mode=="exit"):
            break
        mode=int("0x"+mode,16)
        mode=a^mode
        list.append(hex(mode))
    return list
def zeroXascii(List):
    asciiStr=''
    for i in range(0,len(List)):
        List[i]=chr(int(List[i],16))
        asciiStr+=List[i]
    return asciiStr
a=''
while(True):
    b=input("아무거나 입력(종료:exit):")
    if(b=='exit'):
        break
    a+=zeroXascii(XC())
print(a)