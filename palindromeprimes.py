import sys
sys.setrecursionlimit (30000) 

from palindrome import isPalindrome

def isPrime(startNum,currentNum=2):
    if(startNum<=1):
        return False    
    elif(currentNum>int((startNum+1)/2)):
        return True
    else:
        if(startNum%currentNum==0):
            return False
        else:
            return isPrime(startNum,currentNum+1)

def loopAndCheck(startPoint,endPoint):
    if(startPoint<=endPoint):
        if(isPalindrome(startPoint)):
            if(isPrime(startPoint)):
                print(startPoint)
        loopAndCheck(startPoint+1,endPoint)
    
def main():
    n = int(input('Enter the starting point N:\n'))
    m = int(input('Enter the ending point M:\n'))
    print('The palindromic primes are:')
    loopAndCheck(n,m)
        
if __name__ == '__main__':
    main()