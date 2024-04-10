import os

from py_clob_client.clob_types import (
  ApiCreds, 
  RequestArgs,
)
from py_clob_client.signer import Signer
from dotenv import load_dotenv
from py_clob_client.constants import POLYGON
from py_clob_client.headers.headers import create_level_2_headers
import requests

load_dotenv()

def main():
    host = os.getenv("CLOB_API_URL")
    key = os.getenv("PK")
    creds = ApiCreds(
        api_key=os.getenv("CLOB_API_KEY"),
        api_secret=os.getenv("CLOB_SECRET"),
        api_passphrase=os.getenv("CLOB_PASS_PHRASE"),
    )
    chain_id = POLYGON
    signer = Signer(key, chain_id)

    request_path = "/rewards/user"
    request_args = RequestArgs(method="GET", request_path=request_path)
    headers = create_level_2_headers(signer, creds, request_args)

    url = "{}{}?date={}&signature_type={}".format(host, request_path, "2024-04-10",1)
    print(url)

    resp = requests.request(
        method="GET", url=url, headers=headers
    )

    print(resp.json())



main()