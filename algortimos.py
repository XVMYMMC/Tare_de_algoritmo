def mcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


### Alterando el codigo un poco, más bien el archivo, para así actualizar la cosa.