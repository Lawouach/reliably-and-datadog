import random

from ddtrace import config, patch
import ddtrace.profiling.auto
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


async def index(request: Request) -> JSONResponse:
    if random.random() > 0.94:
        return JSONResponse({'error': 'sigh'}, status_code=400)
    if random.random() > 0.99:
        return JSONResponse({'error': 'booom'}, status_code=500)
    return JSONResponse({'message': 'hello world'})


patch(starlette=True)
config.starlette['distributed_tracing'] = True
config.starlette['service_name'] = 'my-backend-service'

app = Starlette(debug=True, routes=[
    Route('/', index),
])
