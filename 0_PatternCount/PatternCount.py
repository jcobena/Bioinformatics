def main():
    
    with open('dataset_2_6.txt', 'r') as infile:
        
        for i,j in enumerate(infile):
            if i == 0:
                mytext = str(j.strip()) 
                
            else:
                mypat = str(j.strip())
    
    mypatcoyunt = PatternCount(mytext, mypat)
    print(mypatcoyunt)
   
def PatternCount(atext, apattern):
    
    mycounter = 0
    
    lentext = len(atext)
    lenpatt = len(apattern)
    
    for i in range(0, lentext-lenpatt+1, 1):
        if str(atext[i:lenpatt+i]) == apattern:
            mycounter += 1
            
    return mycounter
            
        

if __name__ == "__main__": main()
