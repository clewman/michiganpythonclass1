def computepay(h,r):
    if h>40:
        rate1 = (r*1.5)*(h-40)
    return ((h-5)*r)+rate1
hrs = float(raw_input("Enter Hours:"))
rate = float(raw_input("Enter Rate:"))
p = computepay(hrs,rate)
print ("Pay",p)



#exercise 2
print('Before')
for thing in [9, 11, 15, 4]:
    print(thing)
print('After')

#exercise 3
largest_so_far = -1
print('Before', largest_so_far)
for the_num in [4, 6, 9, 11, 74, 2312312, 351, 1]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print('After', largest_so_far)
