import logging
import os

from notion_client import Client

notion = Client(
    auth=os.getenv('NOTION_TOKEN'),
    log_level=logging.DEBUG
)
