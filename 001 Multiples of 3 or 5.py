n=1000
sum=0
#initialised for 1000 numbers
#adding only those numbers which are multiples of 3 or 5
for i in range(1,n):
    if i%3 ==0 or i%5==0:
        sum=sum+i
    else:
        pass

print(sum)
