import pandas as pd
import pytz
from influxdb import InfluxDBClient
from .base_connection import BaseConnection


class InfluxDBConnection(BaseConnection):

    def __init__(self, host='localhost', port = 8086, username='admin', password=None, database=None, time_zone = 'US/Eastern'):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.time_zone = time_zone

        self.client = InfluxDBClient(
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            database=self.database
        )

    def query(self, query):
        return self.client.query(query)
