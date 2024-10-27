import json
import os

YOUTUBE = {
    "access_token": "ya29.a0AeDClZATqpnJLcdG_2NWC0DJqnYKlT1_leu_mjfpxbKaY43nHepOyhTcpa6HKhK2GD5YvkssYWtAAEyfsnnJtwC1jpSsPezc6qcMkJPQN0WlSppCmVtHNwlTYx3RB9rG8ku6GvlfQY8b76kky-ZXbOF8E0m6QvPc2qmhFstYanXa_emrow1BaCgYKAYgSARMSFQHGX2MiabHLX498l7ehNx8F5KVilA0187",
    "expires": 1730137904.620908,
    "refresh_token": "1//06Fm4WDyy7DwgCgYIARAAGAYSNwF-L9Ir57UadAFPtK2uoTLF5940Q1AVhjcb9MVojd0wIfXkHUv3BBuxkaQpfKikZTpaYs2Zi0U",
    "token_type": "Bearer"
}

def vipboy():
    TOKEN_DATA = os.getenv("TOKEN_DATA")
    if not TOKEN_DATA:
        os.environ["TOKEN_DATA"] = json.dumps(YOUTUBE)
