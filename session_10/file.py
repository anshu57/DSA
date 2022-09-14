# To get all possible substrings
def subsequence(str):
    if len(str)==0:
        return ['']
    else:
        ch = str[0]
        small_list = subsequence(str[1:])
    myans = small_list + [ch+i for i in small_list] 
    return myans


# to print combinations of letters through keypad (2-9)        
def letterCombinations(digits):
    if len(digits) == 0:
        return ['']
    letter_dict = {2 : 'abc',
            3 : 'def',
            4 : 'ghi',
            5 : 'jkl',
            6 : 'mno',
            7 : 'pqrs',
            8 : 'tuv',
            9 : 'qxyz'}



    str_s = letter_dict.get(int(digits[0]))
    ans =[]
    small_list= letterCombinations(digits[1:])
    for i in range(len(str_s)):
        for j in small_list:
            ans.append(str_s[i]+j)
    return ans


# Board path
def boardPath(sn,en):
    if en == 10:
        return 0
    
    count = 0
    if sn == 1:
        count += boardPath(sn+1,en) + boardPath(sn+2,en) + boardPath(sn+3,en) + boardPath(sn+4,en) + boardPath(sn+5,en)
        return
    if sn == 2:
        count += boardPath(sn+1,en)
    if sn == 3:


def allpermut(str, vis, count, myAns, ans):
    if count == len(str):
        myAns.append(ans)
        return
    
    l = len(str)
    for i in range(l):
        if vis[i]==False:
            vis[i] = True
            allpermut(str, vis, count + 1, myAns, ans + str[i])
            vis[i] = False


myAns = []
vis = [False] * 3 
allpermut("abc", vis, 0, myAns, "") 
print(myAns)









