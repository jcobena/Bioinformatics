'''python script to look for a pattern inside a string, 
   then  counts how many times it appears'''
from _testmultiphase import str_const

base_1 = ['A', 'G']
base_2 = ['T', 'C']

def main():
    #------------------------------------------------
    with open('dataset_3_2_1.txt', 'r') as infile:
    
        for i in infile:
            mystring = str(i.strip()) 

    #----------------------------------
    
        #base_1 = ['A', 'G']
        #base_2 = ['T', 'C']
        
        str_complemt = []
        
        for i in mystring:
            if i == base_1[0]:
                #print(i, base_1[0], base_2[0])
                str_complemt.append(base_2[0])
                
            elif i == base_1[1]:
                str_complemt.append(base_2[1])
                
            elif i == base_2[0]:
                str_complemt.append(base_1[0])
                
            elif i == base_2[1]:
                str_complemt.append(base_1[1])
                
        str_complemt_rev = str_complemt.reverse()
            
        
        mycompl = ''.join(str(i) for i in str_complemt)
        #mycompl_inv = mycompl.reverse()
        
        print(mycompl)
        

 
if __name__ == "__main__": main()
