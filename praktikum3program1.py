import time
def main():
    # untuk menampung jumlah laba
    n=[]
    
    # counter
    count = 1
    
    nilai=0
    modal=100000000
 
    # logika
    while count < 9:
        print('Laba bulan ke-', count, nilai)
        n.append(nilai)

        if count==2:
            nilai=modal*1/100
            
        if count==4:
            nilai=modal*5/100
            
        if count==7:
            nilai=modal*2/100
        
        if count == 8 :
            print("Total laba adalah:", sum(n))
            time.sleep(10)
            break
 
        count += 1
 
if __name__=='__main__':
    main()