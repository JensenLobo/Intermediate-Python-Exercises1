def sum():
    counter = 1
    total_sum = 0

    while counter < 6:
        try:
            integer = int(input(f'Enter int #{counter}: '))
            total_sum += integer
            counter += 1
        except ValueError: # checks for anything else beside an integer
            print('Invalid input. Please enter an int.')
    print(f'Your sum is {total_sum}')

sum()