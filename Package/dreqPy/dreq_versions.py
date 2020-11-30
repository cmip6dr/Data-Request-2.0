

import urllib.request
import zipfile

url = 'https://zenodo.org/record/4292261/files/cmip6dr/CMIP6-Data-Request-XML-v01.00.11.zip?download=1'
url = 'https://zenodo.org/record/4292247/files/cmip6dr/CMIP6-Data-Request-XML-v01.00.10.zip?download=1'
save_path = 'CMIP6-Data-Request-XML-v01.00.10.zip'

import requests

def download_url(url, save_path, chunk_size=128):
    r = urllib.request.urlopen(url)
    with open(save_path, 'wb') as fd:
        fd.write(r.read())

def catz(zfile):
    z = zipfile.ZipFile(zfile)
    print ( z.namelist() )
    xfile = [x for x in z.namelist() if x.rpartition('/')[-1] == 'dreq.xml' ]
    assert len(xfile) == 1
    xf = xfile[0]
    ii = z.open( xf )
    for l in ii.readlines()[:5]:
        print(l)


##download_url( url, save_path )


catz(save_path)

