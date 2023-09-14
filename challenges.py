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
print(f"Caesar crypt: {c}")
print(f"Caesar decrypt: {d}")

def vigenere(string: str, key: str, decrypt: bool = False) -> str:
    t = ""
    for i in range(0, len(string)):
      c = string[i]
      k = ord(key[i%len(key)]) if not decrypt else -ord(key[i%len(key)])
      a = ord('A' if c.isupper() else 'a')
      if(c.isalpha()):
        t += chr((ord(c) - a + k) % 26 + a)
      else:
        t += c
    return t
        

v1 = input("Vigenere text: ")
v2 = input("Vigenere key: ")

c = vigenere(v1, v2)
d = vigenere(c, v2, True)
print(f"Vigenere crypt: {c}")
print(f"Vigenere decrypt: {d}")