from db import InfluxDBConnection
import datetime
import pytz
import asyncio
import pandas as pd
import numpy as np
from sympy import isprime
from preprocessing import SatoshiPreprocess


async def process_data(current_timezone, every_seconds):
    conn = InfluxDBConnection(
        host='localhost',
        port=8086,
        username='admin',
        password='123456789',
        database='ws'
    )

    tz_utc = pytz.timezone('UTC')
    preprocess = SatoshiPreprocess()

    while True:
        await asyncio.sleep(every_seconds)

        start_date = (datetime.datetime.now() - datetime.timedelta(minutes=1))
        
        query_start_date = tz_colombia.localize(start_date).astimezone(tz_utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        result = conn.query("SELECT b FROM ws_data WHERE time >= '{}'".format(query_start_date))

        if len(result) > 0:
            df = pd.DataFrame(list(result)[0])
            df['time'] = pd.to_datetime(df['time'])
            df['b'] = df['b'].astype(np.int64)
            df['time'] = df['time'].dt.tz_localize(None).dt.tz_localize('UTC')

            data = preprocess.transform(df)

            print(data)
        

if __name__ == "__main__":
    
    tz_colombia = pytz.timezone('America/Bogota')
    every_seconds = 60
    loop = asyncio.get_event_loop()

    print("[+] Ha iniciado el procesamiento de los datos cada {} segundos.".format(every_seconds))

    try:
        asyncio.ensure_future(process_data(tz_colombia, every_seconds))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("[+] Ha cancelado el procesamiento de los datos")
        loop.close()
    