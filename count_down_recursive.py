def count_down(i):
    print(i)
    if i <= 0:  # base case
        return
    else:       # recursive case
        count_down(i-1)

count_down(10)
