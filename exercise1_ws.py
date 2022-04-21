import asyncio
from numpy import double
import websockets
import logging
import time
import json
import datetime
from db import InfluxDBConnection


logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)


async def collect_data(ws):
    async for websocket in websockets.connect(ws):
        conn = InfluxDBConnection(
            host='localhost',
            port=8086,
            username='admin',
            password='123456789',
            database='Home'
        )

        conn.client.create_database('ws')

        try:
            while True:
                response = await websocket.recv()
                response = json.loads(response)

                #logging.info(response)

                json_body = [
                    {
                        "measurement": "ws_data",
                        "tags": {
                            "type": "satoshi"
                        },
                        "fields": {
                            "a": response['a'],
                            "b": double(response['b'])
                        }
                    }
                ]

                conn.client.write_points(json_body)

        except websockets.ConnectionClosed:
            continue

if __name__ == "__main__":
    
    ws = 'ws://209.126.82.146:8080'

    loop = asyncio.get_event_loop()

    print("[+] Ha iniciado el obtencion de los datos")

    try:
        asyncio.ensure_future(collect_data(ws))
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("[+] Ha cancelado la obtencion de los datos")
        loop.close()
    