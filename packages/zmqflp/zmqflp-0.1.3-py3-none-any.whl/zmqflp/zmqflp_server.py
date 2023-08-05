import asyncio
import sys
import zmq
import zmq.asyncio
import socket
import umsgpack
import logging

class ZMQFLPServer(object):
    def __init__(self, custom_identity = None, str_port = '9001'):
        ctx = zmq.asyncio.Context()
        # Prepare server socket with predictable identity
        if custom_identity:
            identity = custom_identity
        else:
            identity = socket.gethostbyname(socket.gethostname())
        bind_endpoint = "tcp://*:"+str(str_port)
        connect_endpoint = ('tcp://'+identity+':'+str(str_port)).encode('utf8')
        self.server = ctx.socket(zmq.ROUTER)
        self.server.setsockopt(zmq.IDENTITY, connect_endpoint)
        self.server.bind(bind_endpoint)
        logging.info("I: service is ready with identity " + str(connect_endpoint))
        logging.info("I: service is bound to " + str(bind_endpoint))

    async def receive(self):
        # Frame 0: identity of client
        # Frame 1: PING, or client control frame
        # Frame 2: request body
        try:
            request = await self.server.recv_multipart()
            control = request[1].decode('utf8')
        except Exception as e:
            logging.exception(e)
            return # Interrupted
        if control == "PING":
            await self.send([request[0]], "PONG".encode('utf8'), mpack=False)
            return (request[1].decode('utf8'), [request[0]])
        else:
            return (umsgpack.loads(request[2], raw=False), request[0:2])

    async def send(self, orig_req_headers, str_resp, mpack=True):
        out_message = orig_req_headers
        if mpack:
            out_message.append(umsgpack.dumps(str_resp))#.encode('utf8'))
        else:
            out_message.append(str_resp)
        await self.server.send_multipart(out_message)