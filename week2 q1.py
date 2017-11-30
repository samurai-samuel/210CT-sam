import operator



degree1 = input("enter a number a number")
p1 = input("enter  values")
degree2 = input("enter a number")
p2 = input("enetr values")


if degree1 > degree2:
    degree_ans = degree1
 

else:
    degree_ans = degree2

print(degree_ans)   

for d in p1:
  p_ans = d + p2[:]

  print(p_ans)
