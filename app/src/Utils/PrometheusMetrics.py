from prometheus_client import Info, Gauge

from src.Model.SpeedTest.SpeedTest import SpeedTest
from src.Model.SpeedTest.subModels.Ping import NoWorkloadPing, TransferPing
from src.Model.SpeedTest.subModels.Transfer import Transfer
from src.Model.SpeedTest.subModels.Interface import Interface
from src.Model.SpeedTest.subModels.Server import Server
from src.Model.SpeedTest.subModels.Result import Result


class PrometheusMetrics:

    __ping_no_workload_jitter = Gauge('ping_no_workload_jitter', '')
    __ping_no_workload_latency = Gauge('ping_no_workload_latency', '')
    __ping_no_workload_low = Gauge('ping_no_workload_low', '')
    __ping_no_workload_high = Gauge('ping_no_workload_high', '')

    __packet_loss = Gauge('packet_loss', '')

    __download_bandwidth = Gauge('download_bandwidth', '')
    __download_bytes = Gauge('download_bytes', '')
    __download_elapsed = Gauge('download_elapsed', '')
    __download_latency_iqm = Gauge('download_latency_iqm', '')
    __download_latency_low = Gauge('download_latency_low', '')
    __download_latency_high = Gauge('download_latency_high', '')
    __download_latency_jitter = Gauge('download_latency_jitter', '')

    __upload_bandwidth = Gauge('upload_bandwidth', '')
    __upload_bytes = Gauge('upload_bytes', '')
    __upload_elapsed = Gauge('upload_elapsed', '')
    __upload_latency_iqm = Gauge('upload_latency_iqm', '')
    __upload_latency_low = Gauge('upload_latency_low', '')
    __upload_latency_high = Gauge('upload_latency_high', '')
    __upload_latency_jitter = Gauge('upload_latency_jitter', '')

    __isp = Info('isp', 'Internet Service Provider')

    __interface = Info('interface_details','Details of the interface, which was used to test')

    __server = Info('server_details', 'Destination server details')
    __result = Info('result_details', 'SpeedTest details')

    @staticmethod
    def update_metrics(test: SpeedTest):
        PrometheusMetrics.__update_ping_metrics(test.ping)
        PrometheusMetrics.__update_download_metrics(test.download)
        PrometheusMetrics.__update_upload_metrics(test.upload)
        PrometheusMetrics.__update_packet_loss_and_isp(
            test.packet_loss, test.isp)
        PrometheusMetrics.__update_interface(test.interface)
        PrometheusMetrics.__update_server(test.server)
        PrometheusMetrics.__update_result(test.result)

    @staticmethod
    def __update_ping_metrics(obj: NoWorkloadPing):
        PrometheusMetrics.__ping_no_workload_jitter.set(obj.jitter)
        PrometheusMetrics.__ping_no_workload_latency.set(obj.latency)
        PrometheusMetrics.__ping_no_workload_low.set(obj.low)
        PrometheusMetrics.__ping_no_workload_high.set(obj.high)

    @staticmethod
    def __update_download_metrics(obj: Transfer):
        PrometheusMetrics.__download_bandwidth.set(obj.bandwidth)
        PrometheusMetrics.__download_bytes.set(obj.bytes)
        PrometheusMetrics.__download_elapsed.set(obj.elapsed)

        PrometheusMetrics.__update_download_ping(obj.latency)

    @staticmethod
    def __update_download_ping(obj: TransferPing):
        PrometheusMetrics.__download_latency_iqm.set(obj.iqm)
        PrometheusMetrics.__download_latency_low.set(obj.low)
        PrometheusMetrics.__download_latency_high.set(obj.high)
        PrometheusMetrics.__download_latency_jitter.set(obj.jitter)

    @staticmethod
    def __update_upload_metrics(obj: Transfer):
        PrometheusMetrics.__upload_bandwidth.set(obj.bandwidth)
        PrometheusMetrics.__upload_bytes.set(obj.bytes)
        PrometheusMetrics.__upload_elapsed.set(obj.elapsed)

        PrometheusMetrics.__update_upload_ping(obj.latency)

    @staticmethod
    def __update_upload_ping(obj: TransferPing):
        PrometheusMetrics.__upload_latency_iqm.set(obj.iqm)
        PrometheusMetrics.__upload_latency_low.set(obj.low)
        PrometheusMetrics.__upload_latency_high.set(obj.high)
        PrometheusMetrics.__upload_latency_jitter.set(obj.jitter)

    @staticmethod
    def __update_packet_loss_and_isp(packet_loss: float, isp: str):
        PrometheusMetrics.__packet_loss.set(packet_loss)
        PrometheusMetrics.__isp.info({"Name": isp})

    @staticmethod
    def __update_interface(obj: Interface):
        PrometheusMetrics.__interface.info(obj.model_dump())

    @staticmethod
    def __update_server(obj: Server):
        PrometheusMetrics.__server.info(obj.model_dump())

    @staticmethod
    def __update_result(obj: Result):
        PrometheusMetrics.__result.info(obj.model_dump())
