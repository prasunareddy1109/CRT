'''print all factors of  a given number
input : 12
output : 1 2 3 4 6 12'''
'''n = int(input("Enter a number: "))
for i in range(1,n+1):
    if n % i ==0:
        print(i)
        all 12 iterations will occur here'''


'''n = int(input("Enter a number: "))
for i in range(1,n//2+1):
    if n % i ==0:
        print(i)
print(n)
so here factor of number will always be half of the number and the given number so the number os iterations willl get reduced'''
    

'''write a program to check wheather the given number is prime or not '''
'''n = int(input("Enter a number: "))
counter = 0
for i in range(2,n//2+1):
    if n % i == 0:
        counter  += 1
if counter ==0:
     print("prime")
        
else:
    print("not prime")'''



'''start = int(input())
end = int(input())
for n in range(start,end+1):
    counter = 0
    for i in range(2,n//2+1):
        if n % i==0:
            counter +=1
    if counter ==0:
        print(n,end=' ')


n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact*i
print(fact)'''


class solution:
    def reverse(self,x: int ) -> int:
        if x<0:
            x  = -1*x
            rev = int(str(x)[::-1])
            return -1 * rev
        else:
            return int(str(x)[::-1])
        
        









