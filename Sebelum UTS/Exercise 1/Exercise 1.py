def encrypted_password(pwd):
  password = list(pwd)

  asciivalue = list()
  for char in password:
    asciichar = ord(char)
    asciivalue.append(asciichar)

  newpassword = ""
  for num in asciivalue:
    satu = num//26 + 80
    dua = num%26 + 80
    if satu > dua:
      tiga = '+'
    else:
      tiga = '-'

    newpassword = newpassword + chr(satu) + chr(dua) + tiga

  return newpassword

def original_password(pwd):
  password = [pwd[i:i+3] for i in range(0, len(pwd), 3)]

  asciivalue = list()
  for word in password:
    kesatu = ord(word[0]) - 80
    kedua = ord(word[1]) - 80
    nilai = 26 * kesatu + kedua
    asciivalue.append(nilai)

  passwordo = ''
  for i in asciivalue:
    char = chr(i)
    passwordo = passwordo + char

  return passwordo
  
print("Enkripsi Password:")
paswor = "anakanakcerdas2020"
print ("Original Password : " + paswor)
print ("Encrypted Password : " + encrypted_password(paswor))
# Output : Original Password : anakanakcerdas2020
# Output : Encrypted Password : Sc-TV-Sc-TS+Sc-TV-Sc-TS+Se-Sg-TZ-Sf-Sc-T[-Qh-Qf-Qh-Qf-


print("Get Original Password:")
pasword = "Sc-TV-Sc-TS+T[-Sc-TQ+TV-T[-Sf-Sc-T\-Sc-Qh-Qf-Qh-Qf-TS+Sg-Se-Sg-"
print ("Encrypted Password : " + pasword)
print ("Original Password : " + original_password(pasword))
# Output : Encrypted Password : Sc-TV-Sc-TS+T[-Sc-TQ+TV-T[-Sf-Sc-T\-Sc-Qh-Qf-Qh-Qf-TS+Sg-Se-Sg-
# Output : Original Password : anaksainsdata2020kece
