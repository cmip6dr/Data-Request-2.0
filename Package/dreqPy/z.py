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


## this is needed ...
def ex01():
   r = requests.get('https://zenodo.org/api/deposit/depositions',
                  params={'access_token': ACCESS_TOKEN})
   r.status_code

   print( r.json() )

##r = requests.get('https://zenodo.org/api/deposit/depositions', params={'access_token': ACCESS_TOKEN})

headers = {"Content-Type": "application/json"}
params = {'access_token': SB_ACCESS_TOKEN}
r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions',
                   params=params,
                   json={},
                   # Headers are not necessary here since "requests" automatically
                   # adds "Content-Type: application/json", because we're using
                   # the "json=" keyword argument
                   # headers=headers,
                   headers=headers)
r.status_code
print( r.json() )

mr = {
    "conceptrecid": "542200",
    "created": "2020-05-19T11:58:41.606998+00:00",
    "files": [],
    "id": 542201,
    "links": {
        "bucket": "https://zenodo.org/api/files/568377dd-daf8-4235-85e1-a56011ad454b",
        "discard": "https://zenodo.org/api/deposit/depositions/542201/actions/discard",
        "edit": "https://zenodo.org/api/deposit/depositions/542201/actions/edit",
        "files": "https://zenodo.org/api/deposit/depositions/542201/files",
        "html": "https://zenodo.org/deposit/542201",
        "latest_draft": "https://zenodo.org/api/deposit/depositions/542201",
        "latest_draft_html": "https://zenodo.org/deposit/542201",
        "publish": "https://zenodo.org/api/deposit/depositions/542201/actions/publish",
        "self": "https://zenodo.org/api/deposit/depositions/542201"
    },
    "metadata": {
        "prereserve_doi": {
            "doi": "10.5072/zenodo.542201",
            "recid": 542201
        }
    },
    "modified": "2020-05-19T11:58:41.607012+00:00",
    "owner": 12345,
    "record_id": 542201,
    "state": "unsubmitted",
    "submitted": False,
    "title": ""
}

sys.exit(0)
# New API
filename = "my-file.zip"
path = "/path/to/%s" % filename

# The target URL is a combination of the bucket link with the desired filename
# seperated by a slash.
with open(path, "rb") as fp:
    r = requests.put(
        "%s/%s" % (bucket_url, filename),
        data=fp,
        params=params,
    )
r.json()

mr = {
  "key": "my-file.zip",
  "mimetype": "application/zip",
  "checksum": "md5:2942bfabb3d05332b66eb128e0842cff",
  "version_id": "38a724d3-40f1-4b27-b236-ed2e43200f85",
  "size": 13264,
  "created": "2020-02-26T14:20:53.805734+00:00",
  "updated": "2020-02-26T14:20:53.811817+00:00",
  "links": {
    "self": "https://zenodo.org/api/files/44cc40bc-50fd-4107-b347-00838c79f4c1/dummy_example.pdf",
    "version": "https://zenodo.org/api/files/44cc40bc-50fd-4107-b347-00838c79f4c1/dummy_example.pdf?versionId=38a724d3-40f1-4b27-b236-ed2e43200f85",
    "uploads": "https://zenodo.org/api/files/44cc40bc-50fd-4107-b347-00838c79f4c1/dummy_example.pdf?uploads"
  },
  "is_head": true,
  "delete_marker": False
}


r = requests.post('https://zenodo.org/api/deposit/depositions/%s/actions/publish' % deposition_id,
                      params={'access_token': ACCESS_TOKEN} )
r.status_code
