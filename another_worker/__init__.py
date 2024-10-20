from quart import Quart
import asyncio
from hypercorn.config import Config
from hypercorn.asyncio import serve

app = Quart(__name__)
quart_app = asyncio.run(serve(app, Config()))

import another_worker.routes
