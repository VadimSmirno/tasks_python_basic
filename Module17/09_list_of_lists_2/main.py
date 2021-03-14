nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = [i_third for i_first in nice_list
            for i_second in i_first
            for i_third in i_second]
print(new_list)

# зачёт!
