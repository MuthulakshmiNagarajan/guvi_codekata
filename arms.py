l=int(raw_input())

u=int(raw_input())

for num in range(l,u+1):

    order=len(str(num))

    sum=0

    temp=num

    while temp>0:

        d=temp%10

        sum+=d**order

        temp//=10

    if num==sum:

        print(num)
