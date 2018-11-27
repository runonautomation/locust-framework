from argparse import Namespace
from locust import runners as r
import requests

def debug_locust(host, cls):
    opts = Namespace()
    opts.host = host
    opts.num_clients = 1
    opts.hatch_rate = opts.num_clients
    opts.reset_stats=False
    r.locust_runner = \
        r.LocalLocustRunner(locust_classes=cls,
                            options=opts)
    r.locust_runner.start_hatching(wait=True)
    r.locust_runner.greenlet.join()

def disable_ssl_warnings():
    requests.packages.urllib3.disable_warnings()