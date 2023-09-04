# -*- coding:utf-8 -*-
import datetime
import locale


class FormatoFecha():
    def __init__(self):
        locale.setlocale(locale.LC_ALL, '')
        self.TM = datetime.datetime.now()
        # self.dt = {
        #     'dia':self.mf('%A', 3),
        #     'mes-':self.mf('%b'),
        #     'anyo':self.mf('%y'),
        #     'ndia':self.mf('%d'),
        #     'hora':self.mf('%H'),
        #     'min':self.mf('%M'),
        #     'seg':self.mf('%S'),
        #     'mseg':self.mf('%f', 3),
        #     'mes':self.mf('%B')
        # }

    def mf(self, codigo, limite=None):
        mivar = self.TM.strftime(codigo)
        if isinstance(mivar, str):
            mivar = self.no_acentos(mivar)
            if limite is not None:
                mivar = mivar[:limite]
        return mivar

    def no_acentos(self, pal):
        no, acentos = 'aeiou', 'áéíóú'
        for x, letra in enumerate(acentos):
            if letra in pal:
                pal = pal.replace(letra, no[x])
        return pal.replace('.', '')
    
    def formato(self, texto):
        li = [e for e in texto.split('$') if e in self.dt.keys()]
        for e in li:
            print(texto, f"${e}$", self.dt.get(e))
            texto = texto.replace(f"${e}$", self.dt.get(e))
        return texto
    
    def doce_horas(self):
        pass
    

# ff = FormatoFecha()
# forma1 = '$ndia$$mes$ $dia$ $hora$.$min$.$seg$_$mseg$'
# forma2 = ''
# print(ff.formato(forma1))