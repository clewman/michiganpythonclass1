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

print(total);

#part 2
score = input("Enter Score: ")
sc = float(score)
if sc > 1:
    print("Out of range.");
elif sc >= 0.9:
    print("A")
elif sc >= 0.8:
    print("B")
elif sc >= 0.7:
    print("C")
elif sc >= 0.6:
    print("D")
elif sc < 0.6:
    print("F")
