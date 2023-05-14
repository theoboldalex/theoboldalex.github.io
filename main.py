def blast_off(num):
    print(num)
    if num == 0:
        print('BLAST OFF!')
        return

    return blast_off(num - 1)

blast_off(10)
