import app.redirects.toClasses as toClasses
import app.redirects.toGUI as toGUI
import app.classes.server_client_conn.ServerClientSetup as uF
from app.classes.tts.handleTts import TtSHandler
import threading
import app.classes.logging.log as log
import os

"""log"""
log.log(os.path.basename(__file__), log.threading, f"Running on Thread: {threading.currentThread()}")

"""declare .py scripts"""
GUI = toGUI.create_gui()
s_conn = threading.Thread(target=uF.updateFeed)
TtS = threading.Thread(target=TtSHandler)

"""feed"""
posts = []
feed = toClasses.feed_class(posts)

"""start .py scripts"""
s_conn.start()
TtS.start()
GUI.run()
