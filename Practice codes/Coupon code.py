import time

coupon_code = "EAT"
has_coupon = None
coupon = ()

while has_coupon is None:
    coupon = input("Do you have a coupon? (Y/N): ")
    if coupon.lower() == "y":
        has_coupon = True
    elif coupon.lower() == "n":
        has_coupon = False
        print("Too bad LOL")
        time.sleep(1)

if has_coupon:
    while True:
        coupon = input("Please enter your coupon code (press E to escape): ")
        if coupon == coupon_code:
            print("Success! Coupon applied.")
            time.sleep(1)
            coupon = True
            break
        elif coupon == "E":
            print("Yeah that's what I thought! You ain't go no coupon.")
            time.sleep(1)
            has_coupon = False
            break
        else:
            print(f"{coupon} was a nice try, but WRONG!!")