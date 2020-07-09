def match(pattern,word):
    if(not (pattern or word)): #both empty
        return True
    elif((pattern and not word) or (word and not pattern)): #one is empty
        return False
    else:
        return (pattern[0]==word[0] or pattern[0]=='?') and match(pattern[1:],word[1:])
