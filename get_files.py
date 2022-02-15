from baracchino import files
import asyncio

async def main():
    fils = await files.list_files("507dcaffdb9a34b150dcb0a526ecc524f496269600a03efc614ffc1493ef093f")
    print([x.name for x in fils])

asyncio.run(main())
