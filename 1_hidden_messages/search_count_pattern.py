
   
def main():
    
    with open('dataset_2_13.txt', 'r') as infile:
    
        for i,j in enumerate(infile):
            if i == 0:
                mytxt = str(j.strip()) 

            else:
                myk = int(j.strip())
    
    mybfq = BettFreqWords(mytxt, myk)
    
    print(*mybfq)
    

def BettFreqWords(atext,k):
    
    freqpatt = []
    freqmap = FreqTable(atext, k)
    
    #this line finds the max values
    max_keys = [key for key, value in freqmap.items() if value == max(freqmap.values())]
    
    return max_keys
        
        
def FreqTable(atext,k):
    
    freqmap = {}
    n = len(atext)
    
    for i in range(0, n-k+1 ,1):
        apattern = atext[i:i+k]
        
        if apattern in freqmap:
            freqmap[apattern] = freqmap[apattern] + 1
                
        else:
            freqmap[apattern] = 1
            
    #max_keys = [key for key, value in freqmap.items() if value == max(freqmap.values())]
    #return max_keys
    
    return freqmap
            

if __name__ == "__main__": main()
