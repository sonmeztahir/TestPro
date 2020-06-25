

def karsilastir(args, args1):
    olan = args
    gelen = args1
    sayi = 0

    for i in range(0, len(gelen)):

        if olan[i] == gelen[i]:
            i += 1
            sayi += 100/len(gelen)
    return sayi



def yanlis_ekle(args, args1):
    olan = args
    gelen = args1
    sayi = 0
    yanlislar = []

    for i in range(0, len(gelen)):

        if olan[i] == gelen[i]:
            i += 1
            sayi += 100 / len(gelen)
        else:
            j = i+1
            yanlislar.append(j)
    return yanlislar


def analiz(liste, soru_sayisi):
    yanlislar = []
    toplam = len(liste)
    son_liste = []

    for i in liste:#liste içindeki tuple ulaşıldı
        for b in i:#tuple içindeki stringe ulaşıldı
            b = b.replace('[', '').replace(']', '').split(',')#string üzerinde işlem yapıldı
            for a in b:
                yanlislar.append(int(a))

    for i in range(1, soru_sayisi + 1):
        bilen = toplam - yanlislar.count(i)
        basari = (100 * bilen) / toplam
        son_liste.append("{}.Soru: {}".format(i, basari))
    return son_liste