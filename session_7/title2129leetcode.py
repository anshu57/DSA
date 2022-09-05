class Solution:
    def capitalizeTitle(self, title: str) -> str:
        final=''
        words_list = title.split()
        for j in range(len(words_list)):
            l=len(words_list[j])
            ans=''
            if l<=2:
                for ch in words_list[j]:
                    if self.isUpperCase(ch):
                        ans+=self.convertLargeCharacterSmall(ch)
                    else:
                        ans+=ch
            else:
                for i in range(l):
                    if i==0:
                        if self.isLowerCase(words_list[j][i]):
                            ans+=self.convertSmallCharacterLarge(words_list[j][i])
                        else:
                            ans+=words_list[j][i]
                    else:
                        if self.isUpperCase(words_list[j][i]):
                            ans+=self.convertLargeCharacterSmall(words_list[j][i])
                        else:
                            ans+=words_list[j][i]
                        
            if j!=len(words_list)-1:
                final+=ans
                final+=' '
            else:
                final+=ans
        
        return(final)
                    
        
        
    def isUpperCase(self, ch: chr)-> int:
        return (ch>='A' and ch<='Z')

    def isLowerCase(self, ch: chr)-> int:
        return ch>='a' and ch<='z'  
        
    def convertSmallCharacterLarge(self, ch: chr)-> int:
        return(chr(ord(ch)-ord('a')+ord('A')))
    
    def convertLargeCharacterSmall(self, ch: chr)-> int:
        return(chr(ord(ch)-ord('A')+ord('a')))     