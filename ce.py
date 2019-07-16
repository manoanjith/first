import statistics
n=int(input())
a=list(map(int,input().split()))[:n]
print(statistics.median(a))
