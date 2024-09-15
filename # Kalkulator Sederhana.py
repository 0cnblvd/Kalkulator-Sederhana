# Kalkulator Sederhana

print(10*"=")
print("kalkulator sederhana")
print(10*"=" +"\n")

#branch

angka1=float(input("masukan angka 1 = "))
operator= input("operator (+,-,x,/): ")
angka2=float(input("masukan angka 2 = "))

#operasi

if operator == "+":
    hasil = angka1+angka2
    print(f"memiliki hasil {hasil}")
elif operator == "-":
    hasil = angka1-angka2
    print(f"memiliki hasil {hasil}")
elif operator == "x " or operator == "*":
    hasil= angka1*angka2
    print(f"memiliki hasil {hasil}")
elif operator == "/" :
    hasil = angka1/angka2
    print(f"memiliki hasil {hasil}")
else:
    print("kalkulator tidak mengerti input user")

print("DONE")