import requests
import pprint
import json
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from requests.auth import HTTPBasicAuth
# some change
<<<<<<< HEAD
# some more changes
=======
   
>>>>>>> main
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

r = session.get("https://api.dailysmarty.com/posts")

resp_dict = json.loads(r.content.decode('utf-8'))
# pprint.pprint(resp_dict)

# pprint.pprint((resp_dict['posts'])[0])

pprint.pprint((resp_dict['posts'])[0]['url_for_post'])


data = {'name': 'Peter'}
url = "https://api.dailysmarty.com/posts"
# payload = {'some': 'data'}
payload = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.78'}
headers = {}
rsp = session.post(url = url, data=json.dumps(payload), headers = headers)
print(rsp)
if rsp.status_code == 401:
    rsp = session.post(url=url,data=json.dumps(payload), headers = headers, auth=HTTPBasicAuth('user', 'pass'))
output = rsp.text
print(output)


auth = HTTPBasicAuth('user', 'pass')

rp = session.get(url, auth = auth)

pprint.pprint(json.loads(rp.content.decode('utf-8')))
print(rp)