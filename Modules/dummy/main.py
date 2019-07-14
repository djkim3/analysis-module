import os
from Modules.dummy.example import test
from socket import *
from Modules.json_socket import Client
from AnalysisModule.config import MODE

class Dummy:
    model = None
    result = None
    path = os.path.dirname(os.path.abspath(__file__))
    host = 'localhost'  # analysis-classifier address
    port = 8333         # analysis-classifier port

    def __init__(self):
        # TODO
        #   - initialize and load model here
        model_path = os.path.join(self.path, "model.txt")
        self.model = open(model_path, "r")
        self.client = Client()

    def inference_by_path(self, image_path):
        result = []
        # TODO
        #   - Inference using image path
        import time
        time.sleep(2)
        result = [[(0, 0, 0, 0), {'TEST': 0.95, 'DEBUG': 0.05}], [(100, 100, 100, 100), {'TEST': 0.95, 'DEBUG': 0.05}]]
        self.result = result

        if MODE == 'CCTV' :
            self.client.connect(self.host, self.port).send({'result': result})
        return self.result
