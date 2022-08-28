# sorted string compress
def compressStr(str):
    si=1
    ei=len(str)-1
    ans_start = str[0]
    ans_last = ''
    while si<=ei:
        if str[si]!=str[si-1]:
            ans_start+=str[si]
        if str[ei]!=str[ei-1]:
            ans_last+=str[ei]
        si+=1
        ei-=1
    ans_start=ans_start+ans_last[-1::-1]
    return(ans_start)
print(compressStr('aaaabbcccdeffg'))
