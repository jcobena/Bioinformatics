'''python script to look for a pattern inside a string, 
   then  counts how many times it appears'''



def main():
    
    with open('dataset_2_13.txt', 'r') as infile:
    
        for i,j in enumerate(infile):
            if i == 0:
                mystring = str(j.strip()) 
    
            else:
                myinteger = int(j.strip())
        
        lenstring = len(mystring)
        freq_table = {}
        
        for i in range(0, lenstring, 1):
            alst = []
            bodytest = []
    
            #get first element
            myorigin = mystring[i]
            alst.append(myorigin)   
            
            #get the other k-1 elements 
            m = i + 1
            n = i + myinteger   #len(mypattern) #because last element is not counted
            
            tmp_lst = mystring[m:n]  
   
            for j in tmp_lst:
                bodytest.append(j)
        
            for k in bodytest:
                alst.append(k)
                
            str1 = ''.join(alst)
            
            if str1 in freq_table:
                freq_table[str1] = freq_table[str1] + 1
                
            else:
                freq_table[str1] = 1
            
        max_keys = [key for key, value in freq_table.items() if value == max(freq_table.values())]
            
        print(*max_keys)
 
if __name__ == "__main__": main()
