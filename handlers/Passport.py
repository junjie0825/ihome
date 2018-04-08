import logging
from .BaseHandler import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        logging.debug("debug msg")
        logging.info("info msg")
        logging.warning("warning msg")
        logging.error("error msg")
        print("pring msg")
        self.write("hello itcast")
