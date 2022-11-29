from tkinter import *
import calcola
# functools modulo per poter inserire parametri in un pulsante can partial
from functools import partial

# liste dove verranno inserite i numeri e gli operatori
lista_numeri = []
lista_operatori = []

# lista dove sarà scritta le operazione digitate
operazione = []

# lista numeri decimali per il confronto
numeri_decimali = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

numero_momentaneo = 0

root = Tk()
root.title("Calcolatrice di Eric")
root.geometry('280x280')

tasto_reset = BooleanVar(root, True)

ris_lab = Label(root, bg="white")
ris_lab.pack()
ris_lab.place(x=1, y=230)
ris_lab["width"] = 30

numeri = StringVar()

numeri_lab = Entry(root, width=37, textvariable=numeri)
numeri_lab.pack()
numeri_lab.place(x=1, y=1)

operatore = StringVar()
operatore_digitato = StringVar()


# funzione che accoda i numeri digitati
def digita_valori(x, finale=0):
    global numero_momentaneo
    tasto_reset.set(False)

    cambia_tasto_cancella()

    if finale == 0:
        if numero_momentaneo == 0:
            numeri.set(x)
            numero_momentaneo = numeri.get()
        else:
            numeri.set(str(numero_momentaneo) + x)
            numero_momentaneo = numeri.get()

    if finale != 0:
        numeri.set(str(finale))


# funzione che salva e chiama le operazioni nel modulo calcolatrice
def salva_calcola(num, ope):
    global lista_numeri
    # global lista_operatori

    numeri.set(controlla_numero(num.get()))

    if '=' in lista_operatori:
        lista_numeri = []
        lista_operatori.pop(-1)

    lista_numeri.append(float(numeri.get()))
    lista_operatori.append(operatore.get())
    operazione.append(numeri.get())
    operazione.append(operatore.get())
    canc()
    numeri.set(calcola.main(lista_numeri, lista_operatori))


# funzione che prende i numeri e gli operazione da svolgere
def operazione_da_svogere(op):
    operatore.set(op)
    salva_calcola(numeri, operatore)
    stampa_operazione(operazione)


# funzione che stampa a video le operazioni che vengono digitate
def stampa_operazione(lista_operazione):
    global operazione
    lista = ''
    for lis in lista_operazione:
        lista = lista + str(lis)
        conto = len(lista)
        if conto >= 37:
            operazione = []
            lista = ''

    ris_lab["text"] = lista


# funzione che controlla se non è stato inserito un numero
def controlla_numero(numero_controllare):
    num_moment = ''
    conta_numeri_decimali = 0

    for x in numeri.get():
        if x in numeri_decimali:
            conta_numeri_decimali += 1
            if conta_numeri_decimali >= 1:
                num_moment = num_moment + x
        if conta_numeri_decimali == 0:
            num_moment = '0'

    return num_moment


# funzioni per la cancellazione dei numeri e degli operatori
def canc():
    global numero_momentaneo
    numero_momentaneo = 0
    numeri.set("")
    operatore.set("")


def cancella_ultimo_numero():
    global numero_momentaneo
    numero_momentaneo = 0
    numeri.set('')
    cambia_tasto_cancella()


def cancella_tutto():
    global numero_momentaneo
    global lista_numeri
    global lista_operatori
    global operazione

    lista_numeri = []
    lista_operatori = []
    operazione = []
    stampa_operazione('')
    numero_momentaneo = 0
    numeri.set("")
    operatore.set("")


# funzione che cambia lo stato del pulsante cancella
def cambia_tasto_cancella():
    if tasto_reset.get() == True:
        cancella = Button(root, text="AC", fg="blue", font=("helvetica", 12), command=cancella_tutto)
        cancella.pack()
        cancella.place(x=200, y=130)
        cancella["width"] = 2
    else:
        # global tasto_reset
        cancella2 = Button(root, text="C", fg="blue", font=("helvetica", 12), command=cancella_ultimo_numero)
        cancella2.pack()
        cancella2.place(x=200, y=130)
        cancella2["width"] = 2
        tasto_reset.set(True)


# funzione per il risultato finale
def risultato():
    global lista_numeri
    global lista_operatori
    global numeri

    numeri.set(controlla_numero(numeri.get()))
    operatore.set('=')
    lista_operatori.append(operatore.get())
    lista_numeri.append(float(numeri.get()))
    operazione.append(numeri.get())
    operazione.append(operatore.get())
    stampa_operazione(operazione)

    conta_uguale = lista_operatori.count('=')
    if conta_uguale >= 2:
        lista_operatori.pop()
        canc()

    else:
        elabora_operazione = calcola.main(lista_numeri, lista_operatori)

        lista_operatori = []
        lista_numeri = []
        canc()
        digita_valori("", elabora_operazione)


# bottoni numerici
uno = Button(root, text="1", fg="red", font=("helvetica", 12), command=partial(digita_valori, "1"))
uno.pack()
uno.place(x=10, y=130)
uno["width"] = 3

due = Button(root, text="2", fg="red", font=("helvetica", 12), command=partial(digita_valori, "2"))
due.pack()
due.place(x=60, y=130)
due["width"] = 3

tre = Button(root, text="3", fg="red", font=("helvetica", 12), command=partial(digita_valori, "3"))
tre.pack()
tre.place(x=110, y=130)
tre["width"] = 3

quattro = Button(root, text="4", fg="red", font=("helvetica", 12), command=partial(digita_valori, "4"))
quattro.pack()
quattro.place(x=10, y=80)
quattro["width"] = 3

cinque = Button(root, text="5", fg="red", font=("helvetica", 12), command=partial(digita_valori, "5"))
cinque.pack()
cinque.place(x=60, y=80)
cinque["width"] = 3

sei = Button(root, text="6", fg="red", font=("helvetica", 12), command=partial(digita_valori, "6"))
sei.pack()
sei.place(x=110, y=80)
sei["width"] = 3

sette = Button(root, text="7", fg="red", font=("helvetica", 12), command=partial(digita_valori, "7"))
sette.pack()
sette.place(x=10, y=30)
sette["width"] = 3

otto = Button(root, text="8", fg="red", font=("helvetica", 12), command=partial(digita_valori, "8"))
otto.pack()
otto.place(x=60, y=30)
otto["width"] = 3

nove = Button(root, text="9", fg="red", font=("helvetica", 12), command=partial(digita_valori, "9"))
nove.pack()
nove.place(x=110, y=30)
nove["width"] = 3

zero = Button(root, text="0", fg="red", font=("helvetica", 12), command=partial(digita_valori, "0"))
zero.pack()
zero.place(x=10, y=180)
zero["width"] = 5

# Bottoni speciali

virgola = Button(root, text=",", fg="red", font=("helvetica", 12), command=partial(digita_valori, "."))
virgola.pack()
virgola.place(x=80, y=180)
virgola["width"] = 3

cancella = Button(root, text="AC", fg="blue", font=("helvetica", 12), command=cancella_tutto)
cancella.pack()
cancella.place(x=200, y=130)
cancella["width"] = 2

# Bottoni delle operazioni

x = Button(root, text="X", fg="blue", font=("helvetica", 12), command=partial(operazione_da_svogere, "*"))
x.pack()
x.place(x=160, y=30)
x["width"] = 2

diviso = Button(root, text="/", fg="blue", font=("helvetica", 12), command=partial(operazione_da_svogere, ":"))
diviso.pack()
diviso.place(x=200, y=30)
diviso["width"] = 2

più = Button(root, text="+", fg="blue", font=("helvetica", 12), command=partial(operazione_da_svogere, "+"))
più.pack()
più.place(x=160, y=80)
più["width"] = 2

meno = Button(root, text="-", fg="blue", font=("helvetica", 12, "bold"), command=partial(operazione_da_svogere, "-"))
meno.pack()
meno.place(x=200, y=80)
meno["width"] = 2

uguale = Button(root, text="=", fg="blue", font=("helvetica", 12), command=risultato)
uguale.pack()
uguale.place(x=160, y=130)
uguale["width"] = 2

percentuale = Button(root, text="%", fg="blue", font=("helvetica", 12), command=partial(operazione_da_svogere, "%"))
percentuale.pack()
percentuale.place(x=200, y=180)
percentuale["width"] = 2

# bottoni extra
radice_quadrata = Button(root, text="√", fg="blue", font=("helvetica", 12),
                         command=partial(operazione_da_svogere, "sqr"))
radice_quadrata.pack()
radice_quadrata.place(x=160, y=180)
radice_quadrata["width"] = 2

# chiamata alla funzione del tasto cancella
cambia_tasto_cancella()

elevazione_2 = Button(root, text="x²", fg="blue", font=("helvetica", 12), command=partial(operazione_da_svogere, "x²"))
elevazione_2.pack()
elevazione_2.place(x=240, y=30)
elevazione_2["width"] = 2

elevazione_numero = Button(root, text="xʸ", fg="blue", font=("helvetica", 12),
                           command=partial(operazione_da_svogere, "xʸ"))
elevazione_numero.pack()
elevazione_numero.place(x=240, y=80)
elevazione_numero["width"] = 2

trasforma_int = Button(root, text="int", fg="blue", font=("helvetica", 12),
                       command=partial(operazione_da_svogere, "int"))
trasforma_int.pack()
trasforma_int.place(x=240, y=130)
trasforma_int["width"] = 2

trasforma_x_xx = Button(root, text="x.xx", fg="blue", font=("helvetica", 12),
                        command=partial(operazione_da_svogere, "x.xx"))
trasforma_x_xx.pack()
trasforma_x_xx.place(x=240, y=180)
trasforma_x_xx["width"] = 2

root.mainloop()