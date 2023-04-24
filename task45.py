def find_div_sum(num: int) -> int:
    div_sum = 0
    for i in range(1, num//2+1):
        if num % i == 0:
            div_sum += i
    return div_sum


k = int(input())
result = []
for i in range(k):
    second = find_div_sum(i)
    first = find_div_sum(second)
    if i == first and i != second:
        if (second, i) not in result:
            result.append((i, second))
print(result)
