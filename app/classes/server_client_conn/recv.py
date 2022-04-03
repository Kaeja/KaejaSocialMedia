import app.data.basicData as bD
import app.classes.logging.log as log

import pickle
import threading
import os
import time


class recv:
    def __init__(self, cs, addr):
        """Declare vars/start functions"""
        log.log(os.path.basename(__file__), log.threading, f"Running on Thread: {threading.currentThread()}")
        self.cs = bD.socket
        self.addr = addr
        self.HEADER = 1024
        self.FORMAT = "utf-8"
        self.connected = True
        self.loop()

    def loop(self):
        """main recv loop"""
        while True:
            if not bD.connected: log.log(os.path.basename(__file__), log.csh, f"no server connection {bD.connected}")
            self.cs = bD.socket
            try:
                msg_len = int(self.cs.recv(self.HEADER).decode(self.FORMAT))
                msg = pickle.loads(self.cs.recv(msg_len))
                log.log(os.path.basename(__file__), log.csh, f"Received message from Server ({self.addr}): {msg}")
                if isinstance(msg, list):
                    bD.recv_posts = msg
            except:
                pass
