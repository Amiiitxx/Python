a={1,2,3,4,5}
b={3,4,5,6,7}
a.symmetric_difference_update(b)
b.symmetric_difference_update(a)
print(b)
a.symmetric_difference_update(b)
print("a:",a)
print("b:",b)