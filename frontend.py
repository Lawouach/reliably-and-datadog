import random


from ddtrace import config, patch
import ddtrace.profiling.auto
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.routing import Route


async def index(request: Request) -> JSONResponse:
    if random.random() > 0.995:
        return JSONResponse({'error': 'boom'}, status_code=500)
    return JSONResponse({'hello': 'world'})


patch(starlette=True)
config.starlette['distributed_tracing'] = True
config.starlette['service_name'] = 'my-frontend-service'

app = Starlette(debug=True, routes=[
    Route('/', index),
])
