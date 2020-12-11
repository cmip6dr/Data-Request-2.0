import sys

import requests
##r = requests.get("https://zenodo.org/api/deposit/depositions")
##r.status_code

##r.json()

mr = { "message": """The server could not verify that you are authorized to access
  the URL requested. You either supplied the wrong credentials (e.g. a bad
  password), or your browser doesn't understand how to supply the credentials
  required.""",
  "status": 401
}


ii = open( '/home/mjuckes/.local/.zenodo', 'r' )
ACCESS_TOKEN = ii.readline().strip()
print( ACCESS_TOKEN )


#
# ZenodoSandboxDec2020
# https://sandbox.zenodo.org/account/settings/applications/tokens/44717/
#
ii = open( '/home/mjuckes/.local/.zenodo_sandbox', 'r' )
SB_ACCESS_TOKEN = ii.readline().strip()
print( SB_ACCESS_TOKEN )

id_1011 = "4292261"

## this is needed ...
def ex01():
   ##id = "api/deposit/depositions/:2452799"
   url = "https://zenodo.org/api/deposit/depositions/%s" % id_1011
   r = requests.get(url,
                  params={'access_token': ACCESS_TOKEN})
   r.status_code

   print( r.json() )
   return r

