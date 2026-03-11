

'''li = [ 1,2,3,4,5]
res = []
for i in li:
    res.append(i**2)

print(res)


print(" * "*5)
li = ['a','b','c']
res =  ""
for ch in li:
    res = res + ch + " "
print(res)'''



'''1.pyramid
n = 4
output:
   *          
  * *
 * * *
* * * * 

n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
print("----------------")
for i in  range(n,0,-1):
    print(" "*(n-i)+"*"*i)


4.Number pyramid
n = 4 

n = int(input())
li = [1,2,3,4]
for i in range(1,n+1):
    print(" "*(n-i)+"li "*i)'''



n = int(input())
for i in ranga(1,n+1):
    print(" "*(n-i)+" ".join([str(j) for j in range(1,i+1)]))       
















