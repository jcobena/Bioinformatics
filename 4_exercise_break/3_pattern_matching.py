'''python script to look for a pattern inside a string, 
   then  counts how many times it appears'''



def main():
    
    with open('Vibrio_cholerae.txt', 'r') as infile:
    
        for i,j in enumerate(infile):
            if i == 0:
                mygenome = j.strip()
                
            mypattern = 'CTTGATCAT'
    
        # lenstring = len(mystring)
        # freq_table = {}
    
        
        # mygenome = 'GATATATGCATATACTT'
        # mypattern = 'ATAT'
        
        geno_len = len (mygenome)
        patt_len = len(mypattern)
        
        results_lst = []
        
        for i in range(0, geno_len-patt_len, 1):
            alst = []
            bodytest = []
    
            #get first element
            myorigin = mygenome[i]
            alst.append(myorigin)   
            
            #get the other k-1 elements 
            m = i + 1
            n = i + patt_len   #len(mypattern) #because last element is not counted
            
            tmp_lst = mygenome[m:n]  
   
            for j in tmp_lst:
                bodytest.append(j)
        
            for k in bodytest:
                alst.append(k)
                
            str1 = ''.join(alst)
            
            #print(str1)
            
            if str1 == mypattern:
                results_lst.append(i)
                
            
        #     if str1 in freq_table:
        #         freq_table[str1] = freq_table[str1] + 1
        #
        #     else:
        #         freq_table[str1] = 1
        #
        # max_keys = [key for key, value in freq_table.items() if value == max(freq_table.values())]
        #
        # print(*max_keys)
        print(*results_lst)
 
if __name__ == "__main__": main()
