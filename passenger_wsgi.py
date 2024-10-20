import sys
import os
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

sys.path.append(os.getcwd())

from another_worker import app

application = asyncio.run(serve(app, Config(), mode="asgi"))
