import src.Model as Model
import src.Utils as Utils

class SpeedTest:
    def perform_speed_test():
        Utils.PrometheusMetrics.update_metrics(
            Model.SpeedTest(**{
            "type": "result",
            "timestamp": "2024-07-27T17:05:16Z",
            "ping": {
                "jitter": 0.081,
                "latency": 4.324,
                "low": 4.103,
                "high": 4.384
            },
            "download": {
                "bandwidth": 115452305,
                "bytes": 438877216,
                "elapsed": 3811,
                "latency": {
                    "iqm": 14.955,
                    "low": 4.016,
                    "high": 24.555,
                    "jitter": 2.237
                }
            },
            "upload": {
                "bandwidth": 12430178,
                "bytes": 170395788,
                "elapsed": 12300,
                "latency": {
                    "iqm": 3.922,
                    "low": 3.263,
                    "high": 482.980,
                    "jitter": 9.284
                }
            },
            "packetLoss": 0,
            "isp": "Play",
            "interface": {
                "internalIp": "10.0.10.110",
                "name": "eth0",
                "macAddr": "00:15:5D:00:13:04",
                "isVpn": "false",
                "externalIp": "109.243.144.153"
            },
            "server": {
                "id": 37249,
                "host": "speedtest-w5-2.net.play.pl",
                "port": 8080,
                "name": "Play",
                "location": "Warszawa",
                "country": "Poland",
                "ip": "89.108.202.11"
            },
            "result": {
                "id": "95db9c32-330a-49fc-9697-b4f4a5ee8dd1",
                "url": "https://www.speedtest.net/result/c/95db9c32-330a-49fc-9697-b4f4a5ee8dd1",
                "persisted": "true"
            }
        })
        )
    