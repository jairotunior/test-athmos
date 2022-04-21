import os
from time import time
import pandas as pd
from unittest import TestCase
from datasources import JSONDataSource
from pathlib import Path
import time

class TestExercise2(TestCase):
    
    def setUp(self):
        super().setUp()
                
        CURRENT_DIR = Path(__file__).resolve().parent
        filename = 'data.json'
        self.path = CURRENT_DIR / filename

        if os.path.exists(self.path):
            os.remove(self.path)

        df = pd.DataFrame({'nombres': [], 'apellidos': [], 'edad': [], 'email': []})

        input_data_1 = {
            'nombres': "Mike",
            'apellidos': "Ruiz",
            'edad': 38,
            'email': 'mike@gmail.com'
        }

        input_data_2 = {
            'nombres': "John",
            'apellidos': "Doe",
            'edad': 20,
            'email': 'johndoe@gmail.com'
        }

        input_data_3 = {
            'nombres': "Jairo",
            'apellidos': "Rangel",
            'edad': 30,
            'email': 'jrangel@gmail.com'
        }

        df = df.append(input_data_1, ignore_index=True)
        df = df.append(input_data_2, ignore_index=True)
        df = df.append(input_data_3, ignore_index=True)

        df.to_json(self.path)

        self.process_data = JSONDataSource(self.path)

    def tearDown(self):
        os.remove(self.path)

    def test_create(self):
        input_data_1 = {
            'nombres': "Ronaldo",
            'apellidos': "De Asis",
            'edad': 45,
            'email': 'roro@gmail.com'
        }

        self.process_data.create(**input_data_1)

        self.assertEqual(len(self.process_data.df), 4)

    def test_modify(self):
        input_data_3 = {
            'index': 1,
            'nombres': "Julius",
            'apellidos': "Novacrono",
            'edad': 35,
            'email': 'jnova@nova.com'
        }

        self.process_data.modify(**input_data_3)

        nombres = self.process_data.df.iloc[input_data_3['index']]['nombres']
        self.assertEqual(nombres, input_data_3['nombres'])
    
    def test_modify_index_value(self):
        input_data_3 = {
            'index': 10,
            'nombres': "Julius",
            'apellidos': "Novacrono",
            'edad': 35,
            'email': 'jnova@nova.com'
        }

        with self.assertRaises(AssertionError):
            self.process_data.modify(**input_data_3)

    def test_list(self):
        list = self.process_data.get_list()
        self.assertIsInstance(list, pd.DataFrame)

    def test_delete(self):
        items = len(self.process_data.df)
        self.process_data.delete(0)
        self.assertEqual(len(self.process_data.df), items - 1)
    
    def test_delete_index_value(self):
        def func():
            self.process_data.delete(20)

        self.assertRaises(AssertionError, func)

