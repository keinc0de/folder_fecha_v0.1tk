import tkinter as tk
from tkinter import ttk
import json
from pathlib import Path
from pprint import pprint


class NuevoFolderFecha(tk.Tk):
    def __init__(self):
        super(NuevoFolderFecha, self).__init__()
        self._config_nff()

    def _config_nff(self):
        cf = {
            'bg':'white',
            'wv':400,
            'hv':150
        }

        self.geometry(f"{cf.get('wv')}x{cf.get('hv')}")



if __name__=="__main__":
    app = NuevoFolderFecha()
    app.mainloop()