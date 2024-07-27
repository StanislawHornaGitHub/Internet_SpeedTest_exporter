from fastapi import FastAPI
from prometheus_client import make_asgi_app, Gauge

from src.Model.SpeedTest import SpeedTest
from src.Utils.SpeedTestGauges import SpeedTestGauges

metrics_app = make_asgi_app()

app = FastAPI()


@app.route("/metrics")
def update_results(temp):
    print(temp)
    SpeedTestGauges.isp.info({"isp": "Play"
    })

    return metrics_app
