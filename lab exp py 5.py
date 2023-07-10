set_a = set(input("enter a set 1:"))
set_b = set(input("enter a set 2:"))
subset = all(element in set_b for element in set_a)
if(set_a in set_b):
    print("the given is the subset")
else:
    print("the given is not a subset")
