# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
arr = [int(i) for i in input().strip().split()]

arr1 = [int(i) for i in input().strip().split()]

arrsum = []
for i in range(N):
    arrsum.append(arr[i]* arr1[i])

print('{0:.1f}'.format(sum(arrsum)/sum(arr1)))
