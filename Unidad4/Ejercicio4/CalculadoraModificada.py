#Ejercicio 4 - Unidad 4 - VB
from tkinter import *
from tkinter import ttk
from functools import partial

class Imaginario:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def __str__(self):
        return f"{self.real} + {self.imaginario}i"

    def __add__(self, otro):
        real = self.real + otro.real
        imaginario = self.imaginario + otro.imaginario
        return Imaginario(real, imaginario)

    def __sub__(self, otro):
        real = self.real - otro.real
        imaginario = self.imaginario - otro.imaginario
        return Imaginario(real, imaginario)

    def __mul__(self, otro):
        real = self.real * otro.real - self.imaginario * otro.imaginario
        imaginario = self.real * otro.imaginario + self.imaginario * otro.real
        return Imaginario(real, imaginario)

    def __truediv__(self, otro):
        denominador = otro.real**2 + otro.imaginario**2
        real = (self.real * otro.real + self.imaginario * otro.imaginario) / denominador
        imaginario = (self.imaginario * otro.real - self.real * otro.imaginario) / denominador
        return Imaginario(real, imaginario)


class Calculadora:
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.title('Tk-Calculadora')
        mainframe = ttk.Frame(self.__ventana, padding="3 10 3 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__panel = StringVar()
        self.__operador = StringVar()
        self.__operadorAux = None
        self.__primerOperando = None
        self.__segundoOperando = None
        operatorEntry = ttk.Entry(mainframe, width=10, textvariable=self.__operador, justify='center', state='disabled')
        operatorEntry.grid(column=1, row=1, columnspan=1, sticky=(W, E))
        panelEntry = ttk.Entry(mainframe, width=20, textvariable=self.__panel, justify='right', state='disabled')
        panelEntry.grid(column=2, row=1, columnspan=2, sticky=(W, E))
        ttk.Button(mainframe, text='1', command=partial(self.ponerNUMERO, '1')).grid(column=1, row=3, sticky=W)
        ttk.Button(mainframe, text='2', command=partial(self.ponerNUMERO, '2')).grid(column=2, row=3, sticky=W)
        ttk.Button(mainframe, text='3', command=partial(self.ponerNUMERO, '3')).grid(column=3, row=3, sticky=W)
        ttk.Button(mainframe, text='4', command=partial(self.ponerNUMERO, '4')).grid(column=1, row=4, sticky=W)
        ttk.Button(mainframe, text='5', command=partial(self.ponerNUMERO, '5')).grid(column=2, row=4, sticky=W)
        ttk.Button(mainframe, text='6', command=partial(self.ponerNUMERO, '6')).grid(column=3, row=4, sticky=W)
        ttk.Button(mainframe, text='7', command=partial(self.ponerNUMERO, '7')).grid(column=1, row=5, sticky=W)
        ttk.Button(mainframe, text='8', command=partial(self.ponerNUMERO, '8')).grid(column=2, row=5, sticky=W)
        ttk.Button(mainframe, text='9', command=partial(self.ponerNUMERO, '9')).grid(column=3, row=5, sticky=W)
        ttk.Button(mainframe, text='0', command=partial(self.ponerNUMERO, '0')).grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='+', command=partial(self.ponerOPERADOR, '+')).grid(column=2, row=6, sticky=W)
        ttk.Button(mainframe, text='-', command=partial(self.ponerOPERADOR, '-')).grid(column=3, row=6, sticky=W)
        ttk.Button(mainframe, text='*', command=partial(self.ponerOPERADOR, '*')).grid(column=1, row=7, sticky=W)
        ttk.Button(mainframe, text='/', command=partial(self.ponerOPERADOR, '/')).grid(column=2, row=7, sticky=W)
        ttk.Button(mainframe, text='=', command=partial(self.ponerOPERADOR, '=')).grid(column=3, row=7, sticky=W)
        self.__panel.set('0')
        panelEntry.focus()
        self.__ventana.mainloop()

    def ponerNUMERO(self, numero):
        if self.__operadorAux is None:
            valor = self.__panel.get()
            self.__panel.set(valor + numero)
        else:
            self.__operadorAux = None
            valor = self.__panel.get()
            self.__primerOperando = Imaginario(int(valor), int(numero))
            self.__panel.set(numero)

    def borrarPanel(self):
        self.__panel.set('0')

    def resolverOperacion(self, operando1, operacion, operando2):
        resultado = None
        if operacion == '+':
            resultado = operando1 + operando2
        elif operacion == '-':
            resultado = operando1 - operando2
        elif operacion == '*':
            resultado = operando1 * operando2
        elif operacion == '/':
            resultado = operando1 / operando2

        self.__panel.set(str(resultado))

    def ponerOPERADOR(self, op):
        if op == '=':
            operacion = self.__operador.get()
            self.__segundoOperando = Imaginario(int(self.__panel.get()), 0)
            self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
            self.__operador.set('')
            self.__operadorAux = None
        else:
            if self.__operador.get() == '':
                self.__operador.set(op)
                self.__operadorAux = op
            else:
                operacion = self.__operador.get()
                self.__segundoOperando = Imaginario(int(self.__panel.get()), 0)
                self.resolverOperacion(self.__primerOperando, operacion, self.__segundoOperando)
                self.__operador.set(op)
                self.__operadorAux = op


def main():
    calculadora = Calculadora()

if __name__ == '__main__':
    main()
