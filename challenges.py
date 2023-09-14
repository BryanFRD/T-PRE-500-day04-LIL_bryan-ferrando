def cipher(string: str, rot: int) -> str:
  t = ""
  for c in string:
    if(c.isalpha()):
      b = ord('A' if c.isupper() else 'a')
      t += chr((ord(c) - b + rot) % 26 + b)
    else:
      t += c
  return t

i1 = input("Cipher text: ")
i2 = int(input("Cipher key: "))

c = cipher(i1, i2)
d = cipher(c, -i2)
print(c)
print(d)