pwd = "pouyan123@"
while True:
    i=0
    for i in range (1,4):
        entry = input("Enter password")
        if entry == pwd:
            print("✅")
            break
        else:
            print("Incorrect. Please try again")
            pass
    i+=1
    print("Exceeded limit")
    break