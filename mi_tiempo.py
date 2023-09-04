# -*- coding:utf-8 -*-
import datetime
import locale


class MiTiempo:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, '')
        self.TM = datetime.datetime.now()

    def ahora(self):
        return self.TM
    
    def obten_texto(self, codigo):
        return self._limpiar_chars(self.TM.strftime(codigo))
    
    def _limpiar_chars(self, texto):
        chars = {
            '\\':'',
            '/':'-',
            '*':'',
            '|':'',
            '>':'',
            '<':'',
            ':':'.'
        }
        for c, v in chars.items():
            texto = texto.replace(c, v)
        return texto