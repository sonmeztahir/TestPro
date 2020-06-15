

def karsilastir(args, args1):
    olan = args
    gelen = args1
    sayi = 0

    for i in range(0, len(gelen)):

        if olan[i] == gelen[i]:
            i += 1
            sayi += 100/len(gelen)
    return sayi