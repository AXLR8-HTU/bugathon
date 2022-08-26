def findPrimeFactors(num):
    
    arr = [];

    for i in range(2,num):
        let isPrime;
        if num % i == 0:
            isPrime = true
       
            for j in range(2,i):
            
                if i % j == 0 :
                    isPrime == false
            

            if isPrime == true: 
                arr.add(i)

    return arr.length
