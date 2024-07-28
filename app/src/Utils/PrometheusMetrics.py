from prometheus_client import Info, Gauge

from src.Model.SpeedTest.subModels.Ping import NoWorkloadPing, TransferPing
from src.Model.SpeedTest.subModels.Transfer import Transfer
from src.Model.SpeedTest.subModels.Interface import Interface
from src.Model.SpeedTest.subModels.Server import Server
from src.Model.SpeedTest.subModels.Result import Result

from src.Model.SpeedTest.SpeedTest import SpeedTest

class PrometheusMetrics:

    __ping_no_workload_jitter = Gauge('ping_no_workload_jitter', '')
    __ping_no_workload_latency = Gauge('ping_no_workload_latency', '')
    __ping_no_workload_low = Gauge('ping_no_workload_low', '')
    __ping_no_workload_high = Gauge('ping_no_workload_high', '')
    
    packet_loss = Gauge('packet_loss', '')

    download_bandwidth = Gauge('download_bandwidth', '')
    download_bytes = Gauge('download_bytes', '')
    download_elapsed = Gauge('download_elapsed', '')
    download_latency_iqm = Gauge('download_latency_iqm', '')
    download_latency_low = Gauge('download_latency_low', '')
    download_latency_high = Gauge('download_latency_high', '')
    download_latency_jitter = Gauge('download_latency_jitter', '')

    upload_bandwidth = Gauge('upload_bandwidth', '')
    upload_bytes = Gauge('upload_bytes', '')
    upload_elapsed = Gauge('upload_elapsed', '')
    upload_latency_iqm = Gauge('upload_latency_iqm', '')
    upload_latency_low = Gauge('upload_latency_low', '')
    upload_latency_high = Gauge('upload_latency_high', '')
    upload_latency_jitter = Gauge('upload_latency_jitter', '')
    
    isp = Info('isp', 'Internet Service Provider')

    interface = Info('interface_details', 'Details of the interface, which was used to test')

    server = Info('server_details', 'Destination server details')
    result = Info('result_details', 'SpeedTest details')

    @staticmethod
    def update_metrics(test: SpeedTest):
        PrometheusMetrics.__update_ping_metrics(test.ping)
        PrometheusMetrics.__update_download_metrics(test.download)
        PrometheusMetrics.__update_upload_metrics(test.upload)
        PrometheusMetrics.__update_packet_loss_and_isp(test.packet_loss, test.isp)
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
        PrometheusMetrics.download_bandwidth.set(obj.bandwidth)
        PrometheusMetrics.download_bytes.set(obj.bytes)
        PrometheusMetrics.download_elapsed.set(obj.elapsed)
        
        PrometheusMetrics.__update_download_ping(obj.latency)
        
    @staticmethod
    def __update_download_ping(obj: TransferPing):
        PrometheusMetrics.download_latency_iqm.set(obj.iqm)
        PrometheusMetrics.download_latency_low.set(obj.low)
        PrometheusMetrics.download_latency_high.set(obj.high)
        PrometheusMetrics.download_latency_jitter.set(obj.jitter)
        
    @staticmethod
    def __update_upload_metrics(obj: Transfer):
        PrometheusMetrics.upload_bandwidth.set(obj.bandwidth)
        PrometheusMetrics.upload_bytes.set(obj.bytes)
        PrometheusMetrics.upload_elapsed.set(obj.elapsed)
        
        PrometheusMetrics.__update_upload_ping(obj.latency)
        
    @staticmethod
    def __update_upload_ping(obj: TransferPing):
        PrometheusMetrics.upload_latency_iqm.set(obj.iqm)
        PrometheusMetrics.upload_latency_low.set(obj.low)
        PrometheusMetrics.upload_latency_high.set(obj.high)
        PrometheusMetrics.upload_latency_jitter.set(obj.jitter)
        
    @staticmethod
    def __update_packet_loss_and_isp(packet_loss: float, isp: str):
        PrometheusMetrics.packet_loss.set(packet_loss)
        PrometheusMetrics.isp.info({"Name":isp})
        
    @staticmethod
    def __update_interface(obj: Interface):
        PrometheusMetrics.interface.info(obj.model_dump())
        
    @staticmethod
    def __update_server(obj: Server):
        PrometheusMetrics.interface.info(obj.model_dump())
        
    @staticmethod
    def __update_result(obj: Result):
        PrometheusMetrics.result.info(obj.model_dump())