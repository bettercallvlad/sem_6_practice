num_list = [1, 2, 1, 3, 4, 5, 3, 4, 1]
pair_count = sum(num_list.count(i)//2 for i in set(num_list))

print(pair_count)
