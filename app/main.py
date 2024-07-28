from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi_utils.tasks import repeat_every
from prometheus_client import make_asgi_app
import src.Controller as Controller

metrics_app = make_asgi_app()


@repeat_every(seconds=60 * 60)
def perform_speed_test():
    Controller.SpeedTest.perform_speed_test()
    print("test performed")


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    Controller.SpeedTest.check_components()
    await perform_speed_test()
    yield
    print("Closing app")

app = FastAPI(lifespan=app_lifespan)

app.mount("/metrics", metrics_app)
