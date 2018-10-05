
    
def solve(n):
    l_count = 0
    for i in range(10000):
        
        if iter(i):
            l_count+=1
    return l_count
        
    
    
    
def iter(n):
    count = 0
    while not isPalindrom(n) and count<50:
        count+=1
        
        n = n + reverse(n)
        
    if isPalindrom(n):
        return False
    
    return True


def reverse(n):
    
    rev = 0
    
    while n!=0:
        rev*=10
        rev+= n%10
        n//=10
    
    return rev



def isPalindrom(n):
    
    if n == reverse(n):
        return True
    
    return False

print(solve(10000))