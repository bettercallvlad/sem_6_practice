first = list(map(int, input().split()))
second = list(map(int, input().split()))

result = [i for i in set(first) if i not in second]
print(result)