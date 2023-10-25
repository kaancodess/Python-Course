while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x / y)

    # except ZeroDivisionError as e:
    #     print("inputs can't be 0")
    #     print(e)

    # except ValueError as e:
    #     print("x and y must be integer")
        
    except Exception as e:
        print("unknown error")
        print(e)
    else:
        print("Everything is OK")
        break
    finally:
        print("finally section is working now")
        break