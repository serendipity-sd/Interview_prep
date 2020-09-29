# Enter your code here. Read input from STDIN. Print output to STDOUT

N =  int(input())
arr = [int(i) for i in input().strip().split() ]

mean = sum(arr)/N

std_list = []
for i in range(len(arr)):
    std_list.append((arr[i] - mean)**2)
print('{0:.1f}'.format((sum(std_list)/N)**(0.5)))
