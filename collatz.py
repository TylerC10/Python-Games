def collatz():
    while True:
        print("Enter a number: ")
        
        try:
            user_num = int(input())
        except ValueError:
            print("Please enter a number only")
            continue
            
        while user_num != 1:
            if user_num % 2 == 0:
                user_num /= 2
                print(user_num)
            else:
                user_num = 3 * user_num + 1
                print(user_num)

        break


collatz()
