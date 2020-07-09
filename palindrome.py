def isPalindrome(s):
    s = str(s)
    if(len(s)<=1):
        return True
    else:
        return s[0]==s[-1] and isPalindrome(s[1:-1])
      
def main():
    inp = input('Enter a string:\n')
    if(isPalindrome(inp)):
        print('Palindrome!')
    else:
        print('Not a palindrome!')
        
if __name__ == '__main__':
    main()