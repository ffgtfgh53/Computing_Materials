import asyncio

async def handle_conn(reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
    writer.write("Connected successfully!\n".encode())
    data = ''
    peer = writer.get_extra_info("peername")
    print("Connected to:", peer)

    try:
        while data != 'exit':
            writer.write("Message: ".encode())
            await writer.drain()
            data = (await reader.read(4096)).decode().rstrip()
            print(f"{peer}: {data!r}")
        writer.write("Ok, exiting now".encode())
        print("Disconnecting", peer)
        writer.close()
        await writer.wait_closed()
        print("Disconnected ", peer)
    except ConnectionResetError as e:
        print("Lost connection", peer)

async def main():
    await asyncio.create_task(asyncio.start_server(handle_conn, '', 12345))

loop = asyncio.new_event_loop()
loop.create_task(main())
try:
    loop.run_forever()
except KeyboardInterrupt:
    print("\nServer stopped")