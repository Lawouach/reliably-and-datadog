import random


from ddtrace import config, patch
import ddtrace.profiling.auto
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


async def index(request: Request) -> JSONResponse:
    if random.random() > 0.994:
        return JSONResponse(
            {'error': 'oh no, you did something bad'}, status_code=400)
    if random.random() > 0.991:
        return JSONResponse(
            {'error': 'oh no, we just bailed'}, status_code=500)
    return JSONResponse({'hello': 'world'})


patch(starlette=True)
config.starlette['distributed_tracing'] = True
config.starlette['service_name'] = 'my-frontend-service'

app = Starlette(debug=True, routes=[
    Route('/', index),
])
