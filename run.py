import asyncio
from subprocess import run
import webbrowser

async def bootup():
    webbrowser.open("http://127.0.0.1:8000")
    await run("py -m uvicorn main:app --reload")

asyncio.run(bootup())