from baracchino import *

async def main():
    key = "507dcaffdb9a34b150dcb0a526ecc524f496269600a03efc614ffc1493ef093f"
    files = await files.list_files(key)
    for f in files:
        print(f"{f}")