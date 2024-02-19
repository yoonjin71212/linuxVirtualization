import requests
import sys
requests.post ('http://daegu.yjlee-dev.pe.kr:32000/create', json = {"req": "req"}, auth = (sys.argv[1], sys.argv[2]))
