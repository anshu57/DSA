def compress(string):
    dict_letter_count={}
    for ch in string:
        if ch in dict_letter_count.keys():
            dict_letter_count[ch]=dict_letter_count.get(ch) + 1
        else:
            dict_letter_count[ch]=1
    l=[]
    for ch,c in dict_letter_count.items():
        if c==1:
            l.append(ch)
        else:
            l.append(ch)
            a=str(c)
            l.append(a)
    return(''.join(l))


print(compress('aaabbcddd'))