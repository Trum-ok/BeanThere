import logging

from pythonjsonlogger.json import JsonFormatter

logger = logging.getLogger("tg-bot")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()
formatter = JsonFormatter(
    "%(asctime)s %(levelname)s %(name)s %(message)s %(command)s %(status)s",
    json_ensure_ascii=False
)
handler.setFormatter(formatter)
logger.addHandler(handler)
