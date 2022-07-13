def main():
    
    with open('dataset_3_5.txt', 'r') as infile:
    
        for i,j in enumerate(infile):
            if i == 0:
                mypattern = j.strip()
    
            else:
                mygenome = j.strip()
    
        geno_len = len (mygenome)
        k = len(mypattern)
        
        results_lst = []
        
        for i in range(0, geno_len-k+1, 1):
            atxt = mygenome[i:i+k]  
            
            if atxt == mypattern:
                results_lst.append(i)
                

        print(*results_lst)
 
if __name__ == "__main__": main()
