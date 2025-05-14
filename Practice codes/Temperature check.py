while True:
    temp = int(input("Enter temperature (-1 to stop): "))

    # Break condition
    if temp == -1:
        print("Stopping input.")
        break
    # Check temperature condition
    elif temp > 30:
        print("Hot")
        pass
    else:
        print("Cool")
        pass