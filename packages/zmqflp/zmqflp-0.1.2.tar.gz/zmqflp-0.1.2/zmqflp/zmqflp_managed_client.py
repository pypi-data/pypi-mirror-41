import time
import umsgpack
import logging
from .zmqflp_api import FreelanceClient

# Client usable with Context Managers
# needed for containerized python jobs

class ZMQFLPManagedClient(object):
    def __init__(self, list_of_server_ips_with_ports_as_str):
        self.client = FreelanceClient()
        time.sleep(0.3) # wait for client to come up
        for ip in list_of_server_ips_with_ports_as_str:
            logging.info('client: connecting to server '+ip)
            self.client.connect("tcp://"+ip)
            logging.info('client: added server '+ip)

    def __enter__(self):
        return self

    def send_and_receive(self, in_request):
        reply = self.client.request(umsgpack.dumps(in_request))
        if not reply:
            logging.info("error, request "+str(in_request)+" unserviced")
            return False
        else:
            return umsgpack.loads(reply[2], encoding="utf-8")
    
    def __exit__(self, *args):
        try:
            print('stopping client...')
            self.client.stop()
        except Exception as e:
            return