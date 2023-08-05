import asyncio
import json

from jsonrpc import JSONRPCResponseManager, dispatcher


@dispatcher.add_method
def foobar(**kwargs):
    return kwargs["foo"] + kwargs["bar"]


@dispatcher.add_method
async def hello_world():
    print("Hello World!")


dispatcher["echo"] = lambda s: s
dispatcher["add"] = lambda a, b: a + b


class JSONRPCProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        peername = transport.get_extra_info('peername')
        print('Connection from {}'.format(peername))
        self.transport = transport

    def data_received(self, data):
        message = data.decode()
        print('Data received: {!r}\n'.format(message))

        request_method, request_message = message.split('\r\n', 1)
        if not request_method.startswith('POST'):
            print('Incorrect HTTP method, should be POST')

        headers, body = request_message.split('\r\n\r\n', 1)
        print('Body: {!r}\n'.format(body))
        data = json.loads(body)
        print(data)

        response = JSONRPCResponseManager.handle(body, dispatcher)
        response_json = json.dumps(response.json).encode('utf-8')

        print('Send: {!r}'.format(response_json))
        self.transport.write(response_json)

        print('Close the client socket')
        self.transport.close()


async def main():
    loop = asyncio.get_running_loop()

    server = await loop.create_server(JSONRPCProtocol, '127.0.0.1', 8880)

    async with server:
        await server.serve_forever()


asyncio.run(main())
