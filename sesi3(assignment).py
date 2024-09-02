def iniFunction(varInt, varFloat, varBool, varString):
    if varInt > len(varString):
        print("Int lebih besar")
    else:
        print("Int lebih kecil")

    while varFloat < varInt:
        print(varFloat)
        varFloat = varFloat + 0.3

    for i in varString:
        print(f"Huruf Besar: {i.upper()}, Huruf Kecil: {i.lower()}")


makanan = {
    "nama": "Ramen",
    "harga": 15000,
    "desc": "Ramen kuah enak, agak pedas"
}

fruits = ["jeruk", "apel", "strawberry", "semangka"]
