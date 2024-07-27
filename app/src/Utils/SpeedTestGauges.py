from prometheus_client import Info, Gauge

class SpeedTestGauges:
    
    ping_no_workload_jitter = Gauge('ping_no_workload_jitter', '')
    ping_no_workload_latency = Gauge('ping_no_workload_latency', '')
    ping_no_workload_low = Gauge('ping_no_workload_low', '')
    ping_no_workload_high = Gauge('ping_no_workload_high', '')
    
    
    download_bandwidth = Gauge('download_bandwidth','')
    download_bytes = Gauge('download_bytes','')
    download_elapsed = Gauge('download_elapsed','')
    download_latency_iqm = Gauge('download_latency_iqm','')
    download_latency_low = Gauge('download_latency_low','')
    download_latency_high = Gauge('download_latency_high','')
    download_latency_jitter = Gauge('download_latency_jitter','')
    
    upload_bandwidth = Gauge('upload_bandwidth','')
    upload_bytes = Gauge('upload_bytes','')
    upload_elapsed = Gauge('upload_elapsed','')
    upload_latency_iqm = Gauge('upload_latency_iqm','')
    upload_latency_low = Gauge('upload_latency_low','')
    upload_latency_high = Gauge('upload_latency_high','')
    upload_latency_jitter = Gauge('upload_latency_jitter','')
    
    
    packet_loss = Gauge('packet_loss','')
    isp = Info('isp','Internet Service Provider')
    
    interface_internal_ip = Gauge('interface_internal_ip','')
    interface_internal_name = Gauge('interface_internal_name','')
    interface_internal_mac_addr = Gauge('interface_internal_mac_addr','')
    interface_internal_is_vpn = Gauge('interface_internal_is_vpn','')
    interface_internal_external_ip = Gauge('interface_internal_external_ip','')
    
    
    server_id = Gauge('server_id','')
    