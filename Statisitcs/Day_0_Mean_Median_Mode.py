N = int(input().strip())

arr = [int(i) for i in input().strip().split(' ')]
arr.sort()

print('{0:.1f}'.format(sum(arr)/N))  # for mean

# for median

if N % 2 == 1:
    print('{0:.1f}'.format(arr[int((N-1)/2)]))
else:
    print('{0:.1f}'.format(0.5*(arr[int(N/2)-1]+arr[int(N/2)])))

# for mode

counts=[]
for i in arr:
    counts.append(arr.count(i))
if max(counts) > 1:
    print(arr[counts.index(max(counts))])
else:
    print(min(arr))


##############################################################################3
#Runtime Error
N = int(input().strip())

arr = [int(i) for i in input().strip().split(' ')]
arr.sort()

print('{0:.1f}'.format(sum(arr)/N))  # for mean

# for median

if N % 2 == 1:
    print('{0:.1f}'.format(arr[int((N-1)/2)]))
else:
    print('{0:.1f}'.format(0.5*(arr[int(N/2)-1]+arr[int(N/2)])))

# for mode

counts=[]
for i in arr:
    counts.append(arr.count(i))
if max(counts) > 1:
    print(arr[counts.index(max(counts))])
else:
    print(min(arr))
