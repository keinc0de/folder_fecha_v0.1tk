# -*- coding:utf-8 -*-
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import os
from mi_tiempo import MiTiempo
import webbrowser


class FolderFecha(tk.Tk):
    def __init__(self):
        super(FolderFecha, self).__init__()
        self._config_ff()

    def _config_ff(self):
        imgs = {
            "folder24_am": "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA7UlEQVRIx2NgoBOQAeJ8IG4ggA3IMdweiD8D8X8i8FsgNiLVgnNEGk62JX9hmrNDhXBiPm6m32iWNOEJynxosIMB3HXXVqngxBt75X6jWUIIf4YGP3EWkGnJOZIsgFmCLyhBGMnMPyRbQAxG88XQtAAWT79pYkFOmBAo7L9DaapZ0ICEkX1DuQXQ/FSPhBloYQFKxFLDgv2wIMFhAVyOXAsc0MofZAuQxcmzAIurcWHaW0BUcQ3DnbniP5GCCDnlIBuKkqJOk1jhwCzBG8nIwAaIv5JhAd5kig7kiaz0Gyx0uSrRci3MB3VImH4AAIz4JcQKp4KFAAAAAElFTkSuQmCC",
            "folder24_ng": "iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAACXBIWXMAAAsSAAALEgHS3X78AAAB1UlEQVRIiaXVvWpUQRQH8N+9m93NKqghiGBnJfgCQoqUaQTBF7AVRLTxBXwFCysrBWt9DQshpZVahIAkoKJxieZeiznjjst+XffAYebOzPn4/+fMuVDrJp3OVzFex22M5pxrY+813qKHs1WD7OEwnDQxTmteP8Ru2A3QX6B/ke6H8ekc51nHMR5hJ2yX0VVXAbXGTzzFj6CglShsYv8uroXhB7wo9trCaYUTvMF7BfzPGM7KIsadyL5Es4zOvTLAEa6Ew2l+BxFk1/L7avErxv1MQYVjqZqO47uEzaRybuJO0FAV+5nu83goVV0zjWC7ODxL5q2XMpTobnG2sYJBKa2EZFb1VPiNrSKRpmsAEg2zHlmmdVwE6HVtE4tkQyqGb3iO71LZd7qDVaWHC+j9D0WlZFpGeICL+IpnEpKa9RAM4uxVk8c3ju8ag3XvIPev41DFvMHpOhSNpAe1GboV65fwxKSnrdQqphUuh5NFHbgtETT4kqEtyLxThS1r16W0gewjXobtI6k1bMb8nNSjSj/eWe2H00QyLe5F0MzAEAexd6Bo+zUeS82pPyPrZTIMH9smJZ7nNQaZzxu4Zf5PXwTv4xNeSZSWD+2+fx9a3ldZvzXMlT82LKwSKbqzUwAAAABJRU5ErkJggg=="
        }
        self.cf = {
            'bg':'#fff',
            'wv':520,
            'hv':250, 
            'archivo rutas':'rutas.txt',
            'mis formatos':'mis_formatos.txt',
            'fo1':('consolas', 8),
            'fo2':('Segoe UI', 10),
            'fo3':('Times new roman', 10),
            'err':'#E12A62',
            'ver1':'#20AC82',
            'ver2':'#004242',
            'def':'#000',
            'az1':'#0021E7',
            'az2':'#3100E7',
            'nar1':'#F07D00',
            'am1':'#E7BD50',
            'am2':'#E7A632',
            'ng1':'#1F2C32',
            'ver0':'#8BC76B',
            'bgt1':'#F0EAD6',
            'ver3':'#042A3B',
            'mor1':'#470962'
        }

        self.geometry(f"{self.cf.get('wv')}x{self.cf.get('hv')}")
        bg = self.cf.get('bg')
        cf = self.cf
        self.config(bg=bg)
        
        # FRAMES
        fr_top = tk.Frame(self, bg=bg)
        fr_top.pack(side='top', expand=1, fill='x')
        fr_d = tk.Frame(fr_top, bg='blue')
        fr_d.pack(side='right', expand=1, fill='x')
        fra = tk.Frame(fr_d, bg=bg)
        fra.pack(side='top', fill='x', expand=1)
        frb = tk.Frame(fr_d, bg=bg)
        frb.pack(side='top', fill='x', expand=1)

        fr_bot = tk.Frame(self, bg='red')
        fr_bot.pack(side='top', fill='both', expand=1)
        fr_bot.columnconfigure(0, weight=1)
        fr_bot.rowconfigure(0, weight=1)
        
        self.img_folder_ng = tk.PhotoImage(data=imgs['folder24_ng'])
        bt_folder = tk.Button(
            fr_top, text='CREAR', image=self.img_folder_ng,
            compound='top', bg='#E7BD50', relief='groove',
            activebackground='#E7A632',
            font=cf.get('fo1')
        )
        bt_folder.pack(side='left')
        self.cmb_rutas = ttk.Combobox(fra)
        self.cmb_rutas.pack(side='left', expand=1, fill='x')
        self.NUEVO_FOLDER = tk.StringVar()
        self.en_new_folder = ttk.Entry(
            frb, textvariable=self.NUEVO_FOLDER, font=cf.get('fo2')
        )
        self.en_new_folder.pack(side='left', fill='x', expand=1)
        self.bt_info = tk.Button(
            frb, text='FORMATO', bg=bg, relief='flat', pady=0,
            font=cf.get('fo1')
        )
        self.bt_info.pack(side='left')
        self.cmb_formato = ttk.Combobox(
            frb, font=cf.get('fo2')
        )
        _cf_bts = {'relief':'groove', 'pady':0, 'font':cf['fo1']}
        self.bt_mas = tk.Button(frb, text='+', width=2, **_cf_bts)
        self.bt_mas.pack(side='left')
        self.cmb_formato.pack(side='left', expand=1, fill='x')
        self.tex = tk.Text(fr_bot, bg='#EAEAE4', font=('consolas', 10))
        self.scroll = tk.Scrollbar(fr_bot, orient='vertical', command=self.tex.yview)
        self.tex.config(yscrollcommand=self.scroll.set, relief='flat')
        self.tex.grid(column=0, row=0, sticky='wens')
        self.scroll.grid(column=1, row=0, sticky='ns')

        self.bt_rmas = tk.Button(fra, text='+', width=2, **_cf_bts)
        self.bt_rmas.pack(side='left')
        self.bt_abrir = tk.Button(fra, text='ABRIR', width=5, command=self.abrir_ruta, **_cf_bts)
        self.bt_abrir.pack(side='left')

        self.rowconfigure(0, weight=1, minsize=32)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1, minsize=24)

        # ESTILOS
        s = ttk.Style()
        s.theme_use('clam')
        s.configure(
            'TEntry', bd=0,
            bordercolor=bg,
            lightcolor=bg,
            selectborderwidth=0,
            fieldbackground=bg,
            selectbackground=bg,
            # selectforeground="red",
            foreground=cf['def']
        )
        s.map(
            'TEntry', lightcolor=[('focus', bg), ('!focus', bg)],
            selectbackground=[('focus', bg), ('!focus', bg)],
            selectforeground=[('focus', 'red'), ('!focus', 'blue')],
        )
        s.configure(
            'TCombobox', selectbackground=cf['def'],
            selectforeground=cf['def'],
            selectedbackground=bg,
            fieldbackground=bg,
            selectborderwidth=0,
            background=bg,
            bordercolor=bg
        )
        s.map(
            'TCombobox', foreground=[('readonly', cf['az2'])],
            selectbackground=[('focus', cf['bg']), ('!focus', bg), ('readonly', bg)],
            fieldbackground=[('focus', bg), ('!focus', bg), ('readonly', bg)],
            selectforeground=[('focus', cf['mor1']), ('!focus', cf['az2'])]
        )
        self.option_add("*TCombobox*Listbox*Background", bg)
        self.option_add('*TCombobox*Listbox*selectBackground', cf['am1'])
        self.option_add('*TCombobox*Listbox*selectForeground', cf['def'])

        # INICIA VALORES
        self.rutas_carga()
        self.mtm = MiTiempo()
        self._misformatos_carga()
        self.cmb_formato.bind('<<ComboboxSelected>>', self.revisa_formato)
        self.cmb_formato.bind('<Return>', self.revisa_formato)
        self.bt_info.config(command=self.muestra_info)
        bt_folder.config(command=self.crear_carpeta)
        self.bt_mas.config(command=self._misformatos_escribe)
        self.bt_rmas.config(command=self._misrutas_escribe)

        self.img_fam = tk.PhotoImage(data=imgs['folder24_am'])
        self.iconphoto(True, self.img_fam)
        self.title('FOLDER FECHA')

        self.ONTOP = tk.BooleanVar(value=False)
        # self.chb_top = tk.Checkbutton(
        #     fra, text='TOP', command=self._sobre, bg=bg, font=cf['fo1'],
        #     relief='flat', variable=self.ONTOP
        # )
        self.chb_top = ttk.Checkbutton(
            fra, text='TOP', command=self._sobre, variable=self.ONTOP
        )
        self.chb_top.pack(side='left')
        s.configure(
            'TCheckbutton',
            indicatorrefief='flat',
            background='white',
        )
        s.map(
            'TCheckbutton',
            indicatorbackground=[('focus', '#C1F1FF'), ('!focus', bg)],
            indicatorcolor=[('focus', 'red'), ('!focus', 'white')]
        )

    def rutas_carga(self):
        archivo_rutas = self.cf.get('archivo rutas')
        if not Path(archivo_rutas).exists():
            with open(archivo_rutas, 'w') as txt:
                txt.write('.\n')
            self.escribe('"rutas.txt" fue creado.\n', self.cf['ver2'])
        lineas = self.lee_archivo(archivo_rutas)
        self.cmb_rutas.config(values=lineas)
        self.cmb_rutas.current(0)
    
    def lee_archivo(self, archivo):
        with open(archivo, 'r') as txt:
            return [l.strip().replace('\n', '') for l in txt.readlines()]

    def escribe(self, texto, estilo):
        self.tex.insert(tk.END, texto, (texto, estilo))
        self.tex.tag_config(estilo, foreground=self.cf.get(estilo))
        self.tex.see(tk.END)
    
    def revisa_formato(self, e=None):
        try:
            formato = self.cmb_formato.get()
            texto = self.mtm.obten_texto(formato)
            self.NUEVO_FOLDER.set(texto)
        except Exception as e:
            self.escribe(f"{e}\n", 'err')
            self.tex.see(tk.END)

    def muestra_info(self):
        d = {
            '%A':'SEMANA dia de la semana\n',
            '%a':'SEMANA dia de la semana abreviado\n',
            '%w':'SEMANA dia de la semana (numero)\n',
            '%d':'MES dia del mes como decimal con cero\n',
            '%B':'MES nombre del mes\n',
            '%b':'MES nombre del mes abreviado\n',
            '%m':'MES numero del mes con cero\n',
            '%Y':'AÑO\n',
            '%y':'AÑO (2 numeros) con cero\n',
            '%H':'HORA 24h con cero\n',
            '%I':'HORA 12h con cero\n',
            '%M':'MINUTOS con cero\n',
            '%S':'SEGUNDOS con cero\n',
            '%j':'NUMERO dia del año con ceros\n',
            '%U':'NUMERO de semana (inicia domingo)\n',
            '%W':'NUMERO de semana (inicia lunes)\n',
            '%c':'representacion fecha y tiempo\n',
            '%x':'representacion fecha\n',
            '%X':'representacion tiempo\n',
            '%%':'%\n'
        }
        for c, v in d.items():
            self.escribe(f"{c:<4}", 'az1')
            self.escribe(' ', 'def')
            self.escribe(v, 'def')

    def crear_carpeta(self):
        nom = self.NUEVO_FOLDER.get()
        if nom!="":
            try:
                folder = Path(self.cmb_rutas.get()).as_posix()
                ruta = f"{folder}/{nom}"
                if Path(ruta).exists():
                    self.escribe("ya existe: ", 'def')
                    self.escribe(f"{nom}\n", 'az1')
                else:
                    os.mkdir(ruta)

                    self.escribe('FOLDER CREADO\n', 'ver2')
                    self.escribe(f"{folder}/", 'def')
                    self.escribe(f"{nom}\n", 'az1')
            except OSError as e:
                self.escribe(f'ERROR: {e}\n', 'err')

    def _misformatos_carga(self):
        archivo_formatos = self.cf.get('mis formatos')
        if not Path(archivo_formatos).exists():
            with open(archivo_formatos, 'w') as txt:
                txt.write('%a %d - %H.%M\n')
            self.escribe(f'"{archivo_formatos}" fue creado.\n', self.cf['ver2'])
        lineas = self.lee_archivo(archivo_formatos)
        self.cmb_formato.config(values=lineas)
        self.cmb_formato.current(0)

    def _misformatos_escribe(self):
        archivo = self.cf.get('mis formatos')
        lineas = self.lee_archivo(archivo)
        new_formato = self.cmb_formato.get()
        if new_formato!='' and new_formato not in lineas:
            lineas.append(new_formato)

            texto = '\n'.join(lineas)
            with open(archivo, 'w') as txt:
                txt.write(texto)
            self._misformatos_carga()
            self.escribe('se guardo ', 'def')
            self.escribe(f'{new_formato}\n', 'ver2')

    def _misrutas_escribe(self):
        archivo = self.cf.get('archivo rutas')
        lineas = self.lee_archivo(archivo)
        new_ruta = self.cmb_rutas.get()
        if new_ruta!='' and new_ruta not in lineas:
            lineas.append(new_ruta)

            texto = '\n'.join(lineas)
            with open(archivo, 'w') as txt:
                txt.write(texto)
            self.rutas_carga()
            self.escribe('se guardo ', 'def')
            self.escribe(f'{new_ruta}\n', 'ver2')

    def abrir_ruta(self):
        try:
            rt = os.path.realpath(self.cmb_rutas.get().strip())
            webbrowser.open(rt)
        except Exception as e:
            self.escribe(f"{e} ->{rt}", self.cf['err'])

    def _sobre(self):
        self.attributes('-topmost', self.ONTOP.get())
        self.update()


if __name__=="__main__":
    app = FolderFecha()
    app.mainloop()