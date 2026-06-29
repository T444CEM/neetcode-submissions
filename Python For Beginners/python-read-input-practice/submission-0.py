def add_two_numbers() -> int:
    user_inp = input()

    nums = [int(i) for i in user_inp.split(",")]

    return sum(nums)



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
