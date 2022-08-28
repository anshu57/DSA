def isUpperCase(ch):
    return ch>='A' and ch<='Z'

def isLowerCase(ch):
    return ch>='a' and ch<='z'
    
def isDigit(ch):
    return ch>='0' and ch<='9'

def convertSmallCharacterLarge(ch):
    return(chr(ord(ch)-ord('a')+ord('A')))
    
def convertLargeCharacterSmall(ch):
    return(chr(ord(ch)-ord('A')+ord('a')))

def lower(str):
    ans =''
    for ch in str:
        if isUpperCase(ch):
            ans+=convertLargeCharacterSmall(ch)
        else:
            ans+=ch
    return(ans)
    

def upper(str):
    ans =''
    for ch in str:
        if isLowerCase(ch):
            ans+=convertSmallCharacterLarge(ch)
        else:
            ans+=ch
    return(ans)


def toggle(str):
    ans =''
    for ch in str:
        if isUpperCase(ch):
            ans+=convertLargeCharacterSmall(ch)
        elif isLowerCase(ch):
            ans+=convertSmallCharacterLarge(ch)
        else:
            ans+=ch
    return(ans)


print(upper('AnshsKH'))

