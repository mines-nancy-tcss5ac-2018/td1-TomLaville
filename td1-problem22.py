values = ["\"","A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M","N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] 


def scoreName(nom): 
    s = 0
    for char in nom:
       
        s+= values.index(char)
    
    return s
    
    
def solve():
    
    noms = [] ##liste qui contient tous les noms    
    ##liste utile pour le score
    

    ##converti le fichier txt en liste de noms
    f = open('p022_names.txt', 'r')
    for l in f:
        noms += l.split(',') ##lis le fichier et sépare les noms par les ',' 
        ##on a donc toujours les ""
 
    ##tri
    noms_tries = sorted(noms, reverse = False)   

    
    ##calcul du score
    score_tot = 0
    for i in range(len(noms_tries)):
        score_tot += (i+1)*scoreName(noms_tries[i])
    
    
    return score_tot


print(solve())


