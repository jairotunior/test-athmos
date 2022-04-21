import os
import pandas as pd
from .base_datasource import BaseDataSource

class JSONDataSource(BaseDataSource):
    def __init__(self, path):
        super().__init__()

        self.list_properties = ['nombres', 'apellidos', 'edad', 'email']
        self.path = path

        self.df = None

        if not os.path.exists(path):
            self.df = pd.DataFrame({ p: [] for p in self.list_properties })
            self._save()
        else:
            self._open()

    def create(self, *args, **kwargs):
        assert kwargs.get('nombres', None) is not None, "El parametro nombres no ha sido suministrado"
        assert kwargs.get('apellidos', None) is not None, "El parametro apellidos no ha sido suministrado"
        assert kwargs.get('edad', None) is not None, "El parametro edad no ha sido suministrado"
        assert kwargs.get('email', None) is not None, "El parametro email no ha sido suministrado"

        new_element = { p: kwargs.get(p) for p in self.list_properties }
        
        self.df = self.df.append(new_element, ignore_index=True)

        self._save()

    def delete(self, index):
        assert index >= 0, "El parametro index debe ser un valor mayor igual a cero."
        index = max(0, index - 1)
        assert len(self.df) > index, "El indice no existe"

        self.df.drop([index], axis=0, inplace=True)

        self._save()

    def modify(self, *args, **kwargs):
        index = kwargs.get('index', None)
        assert index is not None, "No se suministro el parametro index"
        assert index >= 0, "El parametro index debe ser un valor mayor igual a cero."
        index = max(0, index - 1)
        assert len(self.df) > index, "El indice suministrado esta por fuera de la lista."

        self.df.iloc[index] = [kwargs.get(p) for p in self.list_properties]

        self._save()

    def get_list(self):
        return self.df.head()
    
    def _open(self):
        self.df = pd.read_json(self.path)

    def _save(self):
        self.df.to_json(self.path)