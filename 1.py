a = float(input("Write the first number:"))
b = float(input("Write the second number:"))
c = float(input("Write the third number:"))

if (a<b+c) and (b<a+c) and (c<a+b):
          print("the numbers can form a triangle:)")
          if a == b and b ==c:
            print("triangle type: equilateral")
          elif a == b or c == a or b == c:
            print("triangle type: isosceles")
          else:
            print("triangle type: scalene")
else:
    print("the numbers can´t form a triangle:(")            
          
