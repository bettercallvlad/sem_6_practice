num_list = [3, 4, 3, 6, 5, 8, 7]
print(len([num_list[i] for i in range(1, len(num_list)-1)
          if (num_list[i] > num_list[i+1] and
              num_list[i] > num_list[i-1])]))
