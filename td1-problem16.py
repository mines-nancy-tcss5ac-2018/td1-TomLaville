def solve(n):
    ##Calcule la somme des digits du nombre n
    ##Tant que n n'est pas nul on récupère le dernier digit et on effectue un 
    ##décalage sur la droite pour enlever le derner digit.
    s = 0
    while(n!=0):
        s+= n%10
        n = n//10
        
    return s

assert solve(2**15) == 26
print(solve(2**1000))
