def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))
def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
def summator(x, y):
    for i in range(len(SR)):
        rs = []
        for j in range(len(SR[i])):
            rs.append(y[SR[i][j]])
        #print("rs: ", rs)
        l = 0
        for k in range(len(rs)):
            if rs[k] == 1:
                l += 1
        if l % 2 == 0:
            l = 0
        else:
            l = 1
        #print("l: ", l)
        x.append(l)
        #print("rez: ", x)

kreg = int(input("Введите количество регистров: "))
kreg1 = kreg
reg = [0] * kreg

sumat = int(input("Введите количество сумматоров: "))
SR = []
print("Введите перечень регистров для сумматора:")
for i in range(sumat):
    sumreg = input()
    sumreg = sumreg.split()
    for j in range(len(sumreg)):
        sumreg[j] = int(sumreg[j]) - 1
    SR.append(sumreg)
#print("SR", SR)
infsl = input("Введите последовательность, которую необходимо закодировать: ")
infsl1 = infsl
if infsl.isalpha() or infsl.isalnum() and ("2" in infsl or "3" in infsl or "4" in infsl or "5" in infsl or "6" in infsl or "7" in infsl or "8" in infsl or "9" in infsl):
    infsl = text_to_bits(infsl)
print("Информационное слово: ", infsl)
rez = []

while len(infsl) != 0 or kreg != 0:
    if len(infsl) != 0:
        reg.insert(0, int(infsl[0]))
        del reg[-1]
        infsl = infsl.replace(infsl[0], '', 1)
        #print("infsl", infsl)
        #print("reg", reg)
        summator(rez, reg)
    else:
        reg.insert(0, 0)
        del reg[-1]
        #print("infsl", infsl)
        #print("reg", reg)
        summator(rez, reg)
        kreg -= 1
        #print("kreg: ", kreg)

REZ = ""
for i in range(len(rez)):
    REZ += str(rez[i])
print("Кодовое слово: ", REZ)

INFSL = []
while len(REZ) != 0:
    ck = ""
    for i in range(sumat):
        ck += REZ[0]
        REZ = REZ.replace(REZ[0], "", 1)
    #print("ck: ", ck)
    #print("REZ: ", REZ)

    reg1 = []
    for i in range(len(reg)):
        reg1.append(reg[i])
    reg1.insert(0, 0)
    del reg1[-1]
    #print("reg1: ", reg1)
    rez1 = []
    summator(rez1, reg1)

    REZ1 = ""
    for i in range(len(rez1)):
        REZ1 += str(rez1[i])
    #print("REZ1: ", REZ1)

    reg2 = []
    for i in range(len(reg)):
        reg2.append(reg[i])
    reg2.insert(0, 1)
    del reg2[-1]
    #print("reg2: ", reg2)
    rez2 = []
    summator(rez2, reg2)

    REZ2 = ""
    for i in range(len(rez2)):
        REZ2 += str(rez2[i])
    #print("REZ2: ", REZ2)

    if REZ1 == ck and REZ2 != ck:
        INFSL.append(0)
        reg = []
        for i in range(len(reg1)):
            reg.append(reg1[i])
        #print("reg: ", reg)
    elif REZ1 != ck and REZ2 == ck:
        INFSL.append(1)
        reg = []
        for i in range(len(reg2)):
            reg.append(reg2[i])
        #print("reg: ", reg)
    elif len(REZ) == 0:
        INFSL.append(0)
    elif REZ1 == ck and REZ2 == ck:
        reg4 = []
        for i in range(len(reg2)):
            reg4.append(reg2[i])
        reg.insert(0, 0)
        del reg[-1]
        #print("reg: ", reg)
        #reg3 = []
        #for i in range(len(reg1)):
        #    reg3.append(reg1[i])
        #reg4 = []
        #for i in range(len(reg2)):
        #    reg4.append(reg2[i])

        ck = ""
        for i in range(sumat):
            ck += REZ[i]
        #print("ck: ", ck)

        reg1 = []
        for i in range(len(reg)):
            reg1.append(reg[i])
        reg1.insert(0, 0)
        del reg1[-1]
        #print("reg1: ", reg1)
        rez1 = []
        summator(rez1, reg1)

        REZ1 = ""
        for i in range(len(rez1)):
            REZ1 += str(rez1[i])
        #print("REZ1: ", REZ1)

        reg2 = []
        for i in range(len(reg)):
            reg2.append(reg[i])
        reg2.insert(0, 1)
        del reg2[-1]
        #print("reg2: ", reg2)
        rez2 = []
        summator(rez2, reg2)

        REZ2 = ""
        for i in range(len(rez2)):
            REZ2 += str(rez2[i])
        #print("REZ2: ", REZ2)

        if REZ1 == ck or REZ2 == ck:
            INFSL.append(0)
            #print("INFSL: ", INFSL)
            #print("reg: ", reg)
            #print("REZ: ", REZ)
        else:
            reg = []
            for i in range(len(reg4)):
                reg.append(reg4[i])
            INFSL.append(1)
            #print("INFSL: ", INFSL)
            #print("reg: ", reg)
            #print("REZ: ", REZ)

    #print("INFSL: ", INFSL)

IS = ""
for i in range(len(INFSL)):
    IS += str(INFSL[i])
IS = IS[:-kreg1]
print("Изначальное информационное слово: ", IS)
if infsl1.isalpha() or infsl1.isalnum() and ("2" in infsl1 or "3" in infsl1 or "4" in infsl1 or "5" in infsl1 or "6" in infsl1 or "7" in infsl1 or "8" in infsl1 or "9" in infsl1):
    print("Изначальная последовательность: ", text_from_bits(IS))