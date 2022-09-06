def unique_permutations(str, vis, count, myAns,ans):
    if count == len(str):
        myAns.append(ans)
        return
    
    l = len(str)
    prevch = '$'
    for i in range(l):
        if vis[i]==False and str[i]!= prevch:
            prevch = str[i]
            vis[i] = True
            unique_permutations(str, vis, count + 1, myAns, ans + str[i])
            vis[i] = False
    
myAns = []
vis = [False] * 3 
str = ''.join(sorted('aba'))
unique_permutations(str, vis, 0, myAns, "") 
print(myAns)


# leetcode 46 and 47 

def generateStringOnFreq(ch, freq):
    
    return ch*freq


def sortString(str):
    ans = ''
    ch_dict = {}
    for ch in str:
        if ch in ch_dict:
            ch_dict[ch]+=1
        else:
            ch_dict[ch] =1
    for ch in sorted(ch_dict.keys()):
        ans+=generateStringOnFreq(ch,freq)

    return ans


# maizepath

def maizepath(sr,sc,er,ec, ans):
    if sr==er and sc == ec:
        print(ans)
        return

    if sr+1<er: # Horizontal
        maizepath(sr+1,sc,er,ec,ans+'H')
    if sr+1<er and sc+1<ec: # Diagonal
        maizepath(sr+1,sc+1,er,ec,ans+'D')
    if sc+1<ec: # Vertical
        maizepath(sr,sc+1,er,ec,ans+'V')


# maizepath with inf jumps

def maizepath(sr,sc,er,ec, ans):
    if sr==er and sc == ec:
        print(ans)
        return
    for i in range(1,ec+1):
        if sr+i<=er: # Horizontal
            maizepath(sr+i,sc,er,ec,ans+'H'+f'{i}')
        if sr+i<=er and sc+i<ec: # Diagonal
            maizepath(sr+i,sc+i,er,ec,ans+'D'+f'{i}')
        if sc+i<=ec: # Vertical
            maizepath(sr,sc+i,er,ec,ans+'V'+f'{i}') 

      