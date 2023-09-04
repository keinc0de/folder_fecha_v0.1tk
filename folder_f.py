import tkinter as tk
from tkinter import ttk
import json
from pathlib import Path
from pprint import pprint
from formatos import FormatoFecha as ffe
import os


class NuevoFolderFecha(tk.Tk):
    def __init__(self):
        super(NuevoFolderFecha, self).__init__()
        self._config_nff()

    def _config_nff(self):
        self.cf = {
            'bg':'white',
            'wv':450,
            'hv':250, 
            'imgf':'folder_add2.png',
            'archivo rutas':'rutas.txt',
            'fo1':('consolas', 8),
            'serr':'red',
            'sver1':'#20AC82',
            'sver2':'#004242',
            'def1':'#000',
            'saz1':'#0021E7',
            'snar1':'#F07D00'
        }

        
        self.geometry(f"{self.cf.get('wv')}x{self.cf.get('hv')}")
        bg = self.cf.get('bg')
        self.config(bg=bg)
        _pc = {'side':'top', 'expand':1, 'fill':'x'}
        s = ttk.Style()
        s.theme_use('clam')
        self.imgf = tk.PhotoImage(file=self.cf.get('imgf'))
        self.imgf = self.imgf.subsample(4,4)

        fr_top = tk.Frame(self, bg=bg)
        fr_top.pack(side='top', expand=1, fill='x')
        bt_folder = tk.Button(
            fr_top, text='CREAR', image=self.imgf,
            compound='top', bg='#E7BD50', relief='groove',
            activebackground='#E7A632',
            font=('consolas', 8)
        )
        bt_folder.pack(side='left')
        fr_d = tk.Frame(fr_top, bg=bg)
        fr_d.pack(side='left', expand=1, fill='x')

        fra = tk.Frame(fr_d, bg=bg)
        fra.pack(side='top', fill='x', expand=1)

        # self.RUTAS = tk.StringVar()
        # self.cmb_rutas = ttk.Combobox(fra, state='readonly')
        self.cmb_rutas = ttk.Combobox(fra)
        self.cmb_rutas.pack(side='left', expand=1, fill='x')
        # self.cmb_rutas.pack(side='left', fill='x')
        frb = tk.Frame(fr_d, bg=bg)
        frb.pack(side='bottom', fill='x', expand=1)
        # frb.columnconfigure((0), weight=1)

        self.NUEVO_FOLDER = tk.StringVar()
        self.en_new_folder = ttk.Entry(
            frb, textvariable=self.NUEVO_FOLDER, font=self.cf.get('fo1')
        )
        self.en_new_folder.pack(side='left', fill='x', expand=1)

        # self.FORMATO = tk.StringVar()
        # self.en_formato = ttk.Entry(
        #     frb, textvariable=self.FORMATO, font=self.cf.get('fo1')
        # )
        # self.en_formato.pack(side='left', expand=1, fill='x')
        # self.en_formato.bind('<Return>', self.revisa_formato)
        self.bt_info = tk.Button(
            frb, text='FORMATO', bg=bg, relief='flat', pady=0,
            font=self.cf.get('fo1')
        )
        self.bt_info.pack(side='left')
        # wv, hv = self.cf.get('wv'), self.cf.get('hv') 
        # self.bt_info.place(x=wv-80, y=hv-30)
        # self.bt_info.place(x=80, y=30)
        # self.bt_previa = tk.Button(
        #     frb, text='PREVIA', bg=bg, relief='groove'
        # )
        # self.bt_previa.pack(side='left')


        self.FORMATO = tk.StringVar()
        # self.en_formato = ttk.Entry(
        #     frb, textvariable=self.FORMATO, font=self.cf.get('fo1')
        # )
        # self.en_formato.pack(side='left', expand=1, fill='x')
        # self.en_formato.bind('<Return>', self.revisa_formato)

        # COMBO FORMATOSs
        self.cmb_formato = ttk.Combobox(
            frb, font=self.cf.get('fo1')
        )
        self.cmb_formato.pack(side='left', expand=1, fill='x')
        self.cmb_formato.bind('<Return>', self.revisa_formato)

        fr_bot = tk.Frame(self, bg='red')
        fr_bot.pack(side='bottom', fill='x', expand=1)
        self.tex = tk.Text(fr_bot, bg='#EAEAE4', font=('consolas', 10))
        # self.tex.pack(side='left', fill='x', expand=1)
        self.scroll = tk.Scrollbar(fr_bot, orient='vertical', command=self.tex.yview)
        # scroll.pack(side='left', fill='y')
        self.tex.config(yscrollcommand=self.scroll.set, relief='flat')
        fr_bot.columnconfigure(0, weight=10)
        fr_bot.columnconfigure(1, weight=1, minsize=16)
        fr_bot.rowconfigure(1, weight=1)
        self.tex.grid(column=0, row=0, sticky='wens')
        self.scroll.grid(column=1, row=0, sticky='ns')


        self.rowconfigure(0, weight=1, minsize=32)
        self.rowconfigure(1, weight=1, minsize=16)
        # self.rowconfigure(2, weight=10, minsize=16)
        self.columnconfigure(0, weight=10)
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=10)
        fr_bot.rowconfigure(0, weight=1)

        # otros
        self._carga_rutas()

        # St
        s.configure(
            'TEntry', bd=0,
            bordercolor=bg,
            lightcolor=bg,
            selectborderwidth=0,
            fieldbackground=bg,
            selectbackground=bg,
            selectforeground="red",
            foreground='#384182'
        )
        s.map(
            'TEntry', lightcolor=[('focus', bg), ('!focus', bg)],
            selectbackground=[('focus', bg), ('!focus', bg)],
            selectforeground=[('focus', 'gray'), ('!focus', 'blue')],
        )

        s.configure(
            'TCombobox', selectbackground='black',
            selectforeground='black',
            selectedbackground=bg,
            fieldbackground=bg,
            selectborderwidth=0,
            background=bg,
            bordercolor=bg
        )
        s.map(
            'TCombobox', foreground=[('readonly','black')],
            selectbackground=[('focus', bg), ('!focus', bg), ('readonly', bg)],
            fieldbackground=[('focus', bg), ('!focus', bg), ('readonly', bg)],
            selectforeground=[('focus', '#3100E7'), ('!focus', '#1F2C32')]
        )
        bg2 = '#A6FCF7'
        self.option_add("*TCombobox*Listbox*Background", bg)
        self.option_add('*TCombobox*Listbox*selectBackground', bg2)
        self.option_add('*TCombobox*Listbox*selectForeground', 'black')

        # estilos map
        s.configure('TButton',
        background='white',
        foreground='black',
        highlightthickness='0',
        font=('Helvetica', 18, 'bold'))
        s.map('TButton',
        foreground=[('disabled', 'yellow'),
        ('pressed', 'black'),
        ('active', 'black')],
        background=[('disabled', 'gray'),
        ('pressed', '!focus', 'cyan'),
        ('pressed', 'focus', '#F4AE4D'),
        ('active', '#E7BD50')],
        highlightcolor=[('focus', 'orange'),
                        ('!focus', 'red')],
        relief=[('pressed', 'raised'),
        ('!pressed', 'ridge')])

        # bt_folder.config(sty)

        self.bt_info.config(command=self.muestra_info)

        # self.bt_info.place(x=wv-80, y=hv-30)

        self.bt_mas = tk.Button(frb, text='+', relief='groove', pady=0)
        self.bt_mas.pack(side='left')

        bt_folder.config(command=self.crear_carpeta)
        self._carga_formatos()
        self.bt_mas.config(command=self._mis_formatos_escribe)
        self.cmb_formato.bind('<<ComboboxSelected>>', self.revisa_formato)
    
    def _recarga_valores(self):
        rutas = []

    def _carga_rutas(self):
        archivo = self.cf.get('archivo rutas')
        with open(archivo, 'r') as txt:
            lineas = [l.strip().replace('\n', '') for l in txt.readlines()]
        self.cmb_rutas.config(values=lineas)

    def revisa_formato(self, e=None):
        try:
            # print(e.widget.get())
            # print(self.FORMATO.get())
            # print(self.en_formato.get())
            # fun = lambda:self.revisa_formato(e)
            # idf = self.after(500, fun)
            # self.en_formato.after_cancel(idf)


            # formato = self.en_formato.get()
            formato = self.cmb_formato.get()
            texto = ffe().TM.strftime(formato)
            texto = self.limpiar_chars(texto)
            self.NUEVO_FOLDER.set(texto)
        except Exception as e:
            self.escribe(f"{e}\n", 'serr')
            self.tex.see(tk.END)

    def escribe(self, texto, estilo):
        self.tex.insert(tk.END, texto, (texto, estilo))
        self.tex.tag_config(estilo, foreground=self.cf.get(estilo))
        self.tex.see(tk.END)

    def _info_crea(self):
        pass

    def muestra_info(self):
        li = [
            '%a dia de la semana abreviado\n'
        ]
        d = {
            '%A':'SEMANA dia de la semana\n',
            '%a':'SEMANA dia de la semana abreviado\n',
            '%w':'SEMANA dia de la semana (numero)\n',
            '%d':'MES dia del mes como decimal con cero\n',
            # '%-d':'dia del mes como decimal\n',
            '%B':'MES nombre del mes\n',
            '%b':'MES nombre del mes abreviado\n',
            '%m':'MES numero del mes con cero\n',
            # '%-m':'numero del mes\n',
            '%Y':'AÑO\n',
            '%y':'AÑO (2 numeros) con cero\n',
            # '%-y':'año (2 numeros)\n',
            '%H':'HORA 24h con cero\n',
            # '%-H':'hora 24h\n',
            '%I':'HORA 12h con cero\n',
            # '%-I':'hora 12h\n',
            # '%p':'AM o PM\n',
            '%M':'MINUTOS con cero\n',
            # '%-M':'minutos\n',
            '%S':'SEGUNDOS con cero\n',
            # '%-S':'segundos\n',
            '%j':'NUMERO dia del año con ceros\n',
            # '%-j':'numero dia del año\n',
            '%U':'NUMERO de semana (inicia domingo)\n',
            '%W':'NUMERO de semana (inicia lunes)\n',
            '%c':'representacion fecha y tiempo\n',
            '%x':'representacion fecha\n',
            '%X':'representacion tiempo\n',
            '%%':'%\n'
        }
        # for e in li:
        #     self.escribe(e, 'sver1')
        for c, v in d.items():
            self.escribe(f"{c:<4}", 'saz1')
            self.escribe(' ', 'def1')
            self.escribe(v, 'def1')

    def limpiar_chars(self, texto):
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
    
    def crear_carpeta(self):
        nom = self.NUEVO_FOLDER.get()
        if nom!="":
            try:
                folder = Path(self.cmb_rutas.get()).as_posix()
                # self.escribe(f"{nom}\n", 'sver1')
                ruta = f"{folder}/{nom}"
                if Path(ruta).exists():
                    self.escribe("ya existe: ", 'def1')
                    self.escribe(f"{nom}\n", 'saz1')
                else:
                    os.mkdir(ruta)

                    self.escribe('FOLDER CREADO\n', 'sver2')
                    self.escribe(f"{folder}/", 'def1')
                    self.escribe(f"{nom}\n", 'snar1')
            except OSError as e:
                self.escribe(f'ERROR: {e}\n', 'serr')

    def _carga_formatos(self):
        valores = ['', *self._misformatos_lee()]
        self.cmb_formato.config(values=valores)

    def _misformatos_lee(self):
        archivo = 'mis_formatos.txt'
        with open(archivo, 'r') as txt:
            return [l.strip().replace('\n', '') for l in txt.readlines()]
        
    def _mis_formatos_escribe(self):
        archivo = 'mis_formatos.txt'
        lineas = self._misformatos_lee()
        new_formato = self.cmb_formato.get()
        if new_formato!='' and new_formato not in lineas:
            lineas.append(new_formato)

            texto = '\n'.join(lineas)
            with open(archivo, 'w') as txt:
                txt.write(texto)
            self._carga_formatos()
            self.escribe('se guardo ', 'def1')
            self.escribe(f'{new_formato}\n', 'sver2')
        




    


if __name__=="__main__":
    app = NuevoFolderFecha()
    app.mainloop()