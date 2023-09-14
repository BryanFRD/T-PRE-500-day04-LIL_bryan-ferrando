ipt = int(input("Number: "))
print(f"Is equal to 42: {ipt == 42}")
print("This integer is " + "even" if ipt % 2 == 0 else "odd")

ipt2 = input("Password: ")
print("access granted" if ipt2 == "open sesame" else
       "access fucking granted" if ipt2 == "will you open, you goddamn !¤*@¡" else "permission denied")

ipt3 = int(input("Number: "))
if ipt3 == 42 or ipt <= 21 or ipt3%2 == 0 or ipt3/2 < 21 or (ipt3 % 2 == 1 and ipt3 >= 45):
  print("OK")
else:
  print("You got wrong my poor friend")

a = 42
b = 41
if a == b:
  print("A and B are the same")
elif b <= a:
  print("B is equal or lower than A")
elif b != a:
  print("B is different from A")

for i in range(1, 10001):
  print(i)

ipt4 = input("Input: ")
tmp = ""
for c in ipt4:
  tmp+= c+c
print(tmp)

for i in range(10001, 1, -1):
  if(i%7 == 0):
    print(i)

for i in range(-30, 30):
  if i%3 == 0 and i%5 == 0:
    print("FizzBuzz")
  elif i%3 == 0:
    print("Fizz")
  elif i%5 == 0:
    print("Buzz")
  else:
    print(i)
    
for i in range(99, 1, -1):
  print(f"{i} bottles of age appropriate beverages on the wall")

ipt5 = int(input("Number: "))
for i in range(2, int(ipt5/2)+1):
  tmp = ""
  for j in range(ipt5, 0, -1):
    if i*j < ipt5:
      tmp += f"{i*j} "
  print(tmp)

i=int(input("Number: "))
s=input("String: ")
if(i != 0):
  print(i if set("aeiou").intersection(s) else i if i>=42 else s)