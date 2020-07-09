def match(pattern,word):
    if(not (pattern or word)): #both empty
        return True
    elif(not word and pattern=='*'):
        return True
    elif((pattern and not word) or (word and not pattern)): #one is empty
        return False
    else:
        if(pattern[0]=='*'):
            a = [pattern[1:].find('*'),pattern[1:].find('?')]
            a.sort()
            minNum = a[0] and a[1]
            
            if(minNum==-1):
                minNum=len(pattern[1:])
             
            d = word.find(pattern[1:minNum+1])
            
            if(minNum==0):
                return True
            if(d==-1):
                return False
            else:
                return match(pattern[1:],word[d:])
            
        elif(pattern[0]=='?'):
            return match(pattern[1:],word[1:])
        else:
            return pattern[0]==word[0] and match(pattern[1:],word[1:])