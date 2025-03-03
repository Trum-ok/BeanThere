import os
from dotenv import load_dotenv

load_dotenv(override=True)


class Config:
    DEBUG = False
    TG_TOKEN = os.getenv('TG_BOT_TOKEN')
    ADMINS_RAW = os.getenv('ADMINS')

    assert TG_TOKEN is not None, "TG_BOT_TOKEN must be set in .env"
    assert ADMINS_RAW is not None, "ADMINS must be set in .env"

    ADMINS = list(map(int, ADMINS_RAW.split(','))) if ADMINS_RAW else []

    assert len(ADMINS) > 0, "ADMINS list cannot be empty"
