
def triplateSum(arr,n,X):
    count=0
    sum
    for i in range(n):

        for j in range(i+1,n):
            
            for k in range(j+1,n):
                if (arr[i]+arr[j]+arr[k]==X):
                    count+=1
    return count            

a = [1, 2, 4, 3, 6]
n=5
X=10
x=triplateSum(a,n,X)
print(x)