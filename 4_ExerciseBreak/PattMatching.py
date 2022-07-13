def main():
    
    with open('Vibrio_cholerae.txt', 'r') as infile:
        
        results_lst = []
    
        for i,j in enumerate(infile):
            if i == 0:
                mygenome = j.strip()
    
        mypattern = 'CTTGATCAT'
        geno_len = len (mygenome)
        k = len(mypattern)
        
        
        for i in range(0, geno_len-k+1, 1):
            atxt = mygenome[i:i+k]  
            
            if atxt == mypattern:
                results_lst.append(i)
                
        print(*results_lst)
 
if __name__ == "__main__": main()
