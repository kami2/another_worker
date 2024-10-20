from quart import Quart

app = Quart(__name__)

import another_worker.routes