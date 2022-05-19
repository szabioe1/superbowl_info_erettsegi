class Main(object):
    def __init__(self, ssz, datum, gyoztes, eredmeny, vesztes, helyszin, varosallam, nezoszam):
        self.ssz = ssz
        self.datum = datum
        self.gyoztes = gyoztes
        self.eredmeny = eredmeny
        self.vesztes = vesztes
        self.helyszin = helyszin
        self.varosallam = varosallam
        self.nezoszam = nezoszam
with open('SuperBowl.txt', encoding='utf-8') as f:
    data_read = [i.strip().split(';') for i in f.readlines()]
    del data_read[0]
data = []
for i in data_read:
    data.append(Main(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

#4.fel
print('4.feladat: Döntők száma:', len(data))
#5.fel
er1 = 0
er2 = 0
ossz = 0
pontkul = 0
for i in data:
    er1 = i.eredmeny[0:2]
    er2 = i.eredmeny[3:6]
    pontkul = int(er1) - int(er2)
    ossz = ossz + pontkul
atlag = ossz / int(len(data))
print("5.Feladat: Átlagos pontkülönbség:", "%.2f" % atlag)
#6.fel
legn = 0
for i in data:
    if legn < int(i.nezoszam):
        legn = int(i.nezoszam)

for i in data:
    if int(i.nezoszam) == legn:
        er1 = i.eredmeny[0:2]
        er2 = i.eredmeny[3:6]
        print('6.Feladat: Legmagasabb nézőszám a döntők során:\n\tSorszám (Dátum):', i.ssz, '(' + i.datum + ')', '\n\tGyőztes Csapat:', i.gyoztes + ", zerzett pontok:", str(er1), '\n\tVesztes Csapat:', i.vesztes + ', szerzett pontok:', str(er2), '\n\tHelyszín:', i.helyszin, '\n\tVáros, állam:', i.varosallam, '\n\tNézőszám:', i.nezoszam)

#7.fel
c = 0
clubs = []
clubs_count = 0
with open('SuperBowlNew.txt', 'w') as f:
    for i in data:
        c = c + 1
        if i.gyoztes or i.vesztes in clubs:
            clubs.append(i.vesztes)
            clubs.append(i.gyoztes)
            count1 = clubs.count(i.gyoztes)
            count2 = clubs.count(i.vesztes)
            clubs_count = count1 + count2
        f.write(str(c))
        f.write(';')
        f.write(i.datum)
        f.write(i.gyoztes)
        f.write('(')
        f.write(str(count1))
        f.write(')')
        f.write(';')
        f.write(i.eredmeny)
        f.write(';')
        f.write(i.vesztes)
        f.write('(')
        f.write(str(count2))
        f.write(')')
        f.write(';')
        f.write(i.nezoszam)
        f.write('\n')

def romaiszam():
    szam_be = input('szam: ')
    szam = ""
    szam_ossz = 0
    szam = szam_be.upper()
    for i in szam:
        if 'I' in i:
            szam_ossz = szam_ossz + 1
        elif 'V' in i:
            szam_ossz = szam_ossz + 5
        elif 'X' in i:
            szam_ossz = szam_ossz + 10
        elif 'L' in i:
            szam_ossz = szam_ossz + 50
        elif 'C' in i:
            szam_ossz = szam_ossz + 100
        elif 'D' in i:
            szam_ossz = szam_ossz + 500
        elif 'M' in i:
            szam_ossz = szam_ossz + 1000
    print(str(szam_ossz))


romaiszam()
