import requests
import os

from dotenv import load_dotenv
from ebaysdk.finding import Connection as Finding
from ebaysdk.exception import ConnectionError

load_dotenv()

EBAY_APP_ID = os.environ.get('EBAY_APP_ID')  
EBAY_DEV_ID = os.environ.get('EBAY_DEV_ID')  
EBAY_CERT_ID = os.environ.get('EBAY_CERT_ID')

try:
    api = Finding(
        appid=EBAY_APP_ID,
        devid=EBAY_DEV_ID,
        certid=EBAY_CERT_ID,
        config_file=None,
        domain='svcs.sandbox.ebay.com'
    )
    
    response = api.execute('findItemsAdvanced', {'keywords': 'Magic Card'})
    
    print(response.dict())

except ConnectionError as e:
    print(e)
    print(e.response.dict())
