def find_largest(num_list):
    max_num = num_list[0]
    for number in num_list:
        if max_num < number:
            max_num = number
    return max_num
