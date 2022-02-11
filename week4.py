hrs = input("Enter Hours:")
h = float(hrs)
rate = input("enter rate:")
r = float(rate)
if h <=40:
    total = h * r


else:
    ottotal = h - 40
    newtotal = ottotal * r * 1.5
    total = 40 * r + newtotal

print("hi, I'm a test")
print(total);
