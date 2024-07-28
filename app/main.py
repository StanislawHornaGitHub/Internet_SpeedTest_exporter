from fastapi import FastAPI
from prometheus_client import make_asgi_app
from src.Controller.SpeedTest import SpeedTest
import src.Model as Model
from fastapi_utils.tasks import repeat_every
metrics_app = make_asgi_app()

app = FastAPI()

app.mount("/metrics", metrics_app)

# @app.route("/metrics")
# def update_results(temp):
#     SpeedTest.perform_speed_test()

#     return metrics_app


@repeat_every(seconds=10)
def perform_speed_test():
    SpeedTest.perform_speed_test()
    print("test performed")
    
@app.on_event("startup")
async def app_startup():
    await perform_speed_test()