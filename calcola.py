def moltiplica(lista_numeri, lista_operatori):
    risultato = lista_numeri[-2] * lista_numeri[-1]
    lista_numeri.pop()
    lista_numeri.pop()

    if lista_operatori[-1] == '*':
        lista_operatori.pop(-1)
    elif lista_operatori[-2] == '*':
        lista_operatori.pop(-2)
    return risultato


def radice(lista_numeri, lista_operatori):
    risultato = lista_numeri[-1] ** (1 / 2)
    lista_numeri.pop()
    return risultato


def eleva_quadrato(lista_numeri, lista_operatori):
    risultato = lista_numeri[-1] ** 2
    lista_numeri.pop()
    lista_operatori.pop()
    return risultato


def eleva_numero(lista_numeri, lista_operatori):
    risultato = lista_numeri[-2] ** lista_numeri[-1]
    lista_numeri.pop()
    lista_numeri.pop()
    if lista_operatori[-1] == 'xʸ':
        lista_operatori.pop()
    elif lista_operatori[-2] == 'xʸ':
        lista_operatori.pop(-2)
    return risultato


def numero_intero(lista_numeri, lista_operatori):
    risultato = int(lista_numeri[-1])
    lista_numeri.pop()
    lista_operatori.pop()
    return risultato


def virgola_due(lista_numeri, lista_operatori):
    numero_in_striga = str(lista_numeri[-1])
    x = numero_in_striga.split(".")
    risultato = x[0] + "." + x[1][0:2]
    lista_numeri.pop()
    return float(risultato)


def percentuale(lista_numeri, lista_operatori):
    if '+' in lista_operatori:
        risultato = lista_numeri[-2] * lista_numeri[-1] / 100
        risultato = lista_numeri[-2] + risultato
    elif '-' in lista_operatori:
        risultato = lista_numeri[-2] * lista_numeri[-1] / 100
        risultato = lista_numeri[-2] - risultato
    elif lista_operatori[-1] == '%':
        risultato = lista_numeri[-1] / 100
        lista_operatori.append('=')
        return risultato
        
    lista_numeri.pop()
    lista_numeri.pop()
    if lista_operatori[-1] == '%':
        lista_operatori.pop(-1)
        lista_operatori.pop()
        lista_operatori.append('=')
    elif lista_operatori[-2] == '%':
        lista_operatori.pop(-2)
    return risultato


def dividi(lista_numeri, lista_operatori):
    risultato = lista_numeri[-2] / lista_numeri[-1]
    lista_numeri.pop()
    lista_numeri.pop()
    if lista_operatori[-1] == ':':
        lista_operatori.pop(-1)
    elif lista_operatori[-2] == ':':
        lista_operatori.pop(-2)
    return risultato


def somma(lista_numeri):
    risultato = lista_numeri[-2] + lista_numeri[-1]
    lista_numeri.pop()
    lista_numeri.pop()
    return risultato


def sottrai(lista_numeri, lista_operatori):
    risultato = lista_numeri[-2] - lista_numeri[-1]
    lista_numeri.pop()
    lista_numeri.pop()

    return risultato


def main(numeri, operatori):
    while True:

        if operatori[-1] == 'sqr':
            numeri.append(radice(numeri, operatori))
            operatori.append('=')

        elif operatori[-1] == 'x²':
            numeri.append(eleva_quadrato(numeri, operatori))
            operatori.append('=')

        elif operatori[-1] == 'int':
            numeri.append(numero_intero(numeri, operatori))
            operatori.append('=')

        elif operatori[-1] == 'x.xx':
            numeri.append(virgola_due(numeri, operatori))
            operatori.append('=')
        
        conta_operatori = len(operatori)
        if conta_operatori == 1 and operatori[-1] == '%':
            numeri.append(percentuale(numeri, operatori))
        

        if len(numeri) >= 2 and '*' in operatori or len(numeri) >= 2 and ':' in operatori or len(
                numeri) >= 2 and '%' in operatori or len(numeri) >= 2 and 'xʸ' in operatori:

            if operatori[-2] == '*':
                numeri.append(moltiplica(numeri, operatori))

            elif operatori[-2] == ':':
                numeri.append(dividi(numeri, operatori))

            elif operatori[-1] == '%' or operatori[-2] == '+' and operatori[-1] == '%' or operatori[-2] == '-' and \
                    operatori[-1] == '%':
                numeri.append(percentuale(numeri, operatori))


            elif operatori[-2] == 'xʸ':
                numeri.append(eleva_numero(numeri, operatori))

        if len(numeri) >= 2 and len(operatori) >= 2:
            if operatori[-2] == '+' and operatori[-1] == '=' or operatori[-2] == '+' and operatori[-1] == '+' or \
                    operatori[-2] == '+' and operatori[-1] == '-':
                numeri.append(somma(numeri))

            elif operatori[-2] == '-' and operatori[-1] == '=' or operatori[-2] == '-' and operatori[-1] == '-' or \
                    operatori[-2] == '-' and operatori[-1] == '+':
                numeri.append(sottrai(numeri, operatori))

        if operatori[-1] == '=':
            return numeri[-1]
            break

        return numeri[-1]