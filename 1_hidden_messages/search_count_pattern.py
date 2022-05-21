'''python script to look for a pattern inside a string, 
   then  counts how many times it appears'''


def main():
    
    with open('dataset_2_6_3.txt', 'r') as infile:
        mycounter = 0
        
        mylst = []
        for i,j in enumerate(infile):
            if i == 0:
                mystring = str(j.strip()) 
                
            else:
                mypattern = str(j.strip())
                 
        print('mystring = ', mystring) 
        print('mypattern = ', mypattern)
        
        lenstring = len(mystring) - len(mypattern) 
        lastelemt = len(mystring) - len(mypattern)
        
        print('mystring len = ', len(mystring))
        print('mypattern len = ', len(mypattern))
        
        for i in range(0, lenstring, 1):
            alst = []
            bodytest = []
            #print('i value = ', i)
            testorigin = mystring[i]
            alst.append(testorigin)   
            
            m = i + 1
            n = i + len(mypattern) #because last element is not counted
            
            tmp_lst = mystring[m:n]  
   
            for j in tmp_lst:
                bodytest.append(j)
        
            for k in bodytest:
                alst.append(k)
                
            str1 = ''.join(alst)
            #print(str1)
            
            print(str1, mypattern)
            
            if str1 == mypattern:
                mycounter = mycounter+1
                
        print('The pattern {} appears {} times'.format(mypattern, mycounter))
                
            
            
   
                
        

if __name__ == "__main__": main()
