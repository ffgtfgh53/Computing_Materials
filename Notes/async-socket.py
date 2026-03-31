import asyncio

async def handle_conn(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    writer.write("Connected successfully!\n".encode())
    data = ''

    while data != 'exit':
        writer.write("Message: ".encode())
        await writer.drain()
        data = (await reader.read(1024)).decode().rstrip()
        print(f"Got: {data!r}")
    writer.write("Ok, exiting now".encode())
    writer.close()
    await writer.wait_closed()


async def main():
    await asyncio.create_task(asyncio.start_server(handle_conn, '', 12345))

loop = asyncio.new_event_loop()
loop.create_task(main())
loop.run_forever()