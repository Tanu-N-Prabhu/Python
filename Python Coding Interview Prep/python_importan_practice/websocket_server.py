#!/usr/bin/env python

# WS server that sends messages at random intervals
# in browser open websocket_client.html after start the websocket server

import asyncio
import datetime
import random
import websockets


# asynchronise function 
async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + "Z"
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

# create websocket server and call the async function to run
start_server = websockets.serve(time, "127.0.0.1", 5678)
# run the server
asyncio.get_event_loop().run_until_complete(start_server)
# loop the function called for ever
asyncio.get_event_loop().run_forever()