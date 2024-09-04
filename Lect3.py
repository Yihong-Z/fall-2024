import json
import requests
baseURL = "https://api.worldbank.org/V2/country"
group = 'MIC'
format = 'json'
args = {'incomeLevel': group, 'format': format, 'per_page': 1000}
url = baseURL + '?' + '&'.join(['='.join(
                               [key, str(args[key])]) for key in args])
response = requests.get(url)
data = json.loads(response.content)
print(data)

type(data)
len(data[1])
type(data[1][5])
data[1][5]


import zipfile

## example URL:
## https://data.un.org/Handlers/DownloadHandler.ashx?DataFilter=itemCode:526;
##year:2012,2013,2014,2015,2016,2017&DataMartId=FAO&Format=csv&c=2,4,5,6,7&
##s=countryName:asc,elementCode:asc,year:desc
itemCode = 526
baseURL = "https://data.un.org/Handlers/DownloadHandler.ashx"
yrs = ','.join([str(yr) for yr in range(2012,2018)])
filter = f"?DataFilter=itemCode:{itemCode};year:{yrs}"
args1 = "&DataMartId=FAO&Format=csv&c=2,3,4,5,6,7&"
args2 = "s=countryName:asc,elementCode:asc,year:desc"
url = baseURL + filter + args1 + args2
print(url)
## If the website provided a CSV, this would be easier, but it zips the file.
response = requests.get(url)
type(response)
response#200 means the request was successful
response.status_code

import pandas as pd

with io.BytesIO(response.content) as stream:  # create a file-like object
     with zipfile.ZipFile(stream, 'r') as archive:   # treat the object as a zip file
          with archive.open(archive.filelist[0].filename, 'r') as file:  # get a pointer to the embedded file
              dat = pd.read_csv(file)

dat.head()

url = 'http://www.wormbase.org/db/searches/advanced/dumper'

data = {      "specipes":"briggsae",
              "list": "",
              "flank3": "0",
              "flank5": "0",
              "feature": "Gene Models",
              "dump": "Plain TEXT",
              "orientation": "Relative to feature",
              "relative": "Chromsome",
              "DNA":"flanking sequences only",
              ".cgifields" :  "feature, orientation, DNA, dump, relative"
}                                  

response = requests.post(url, data = data)
if response.status_code == 200:
    print("POST request successful")
else:
    print(f"POST request failed with status code: {response.status_code}")
    

hexvals = b'\x4d\x6f\x6d\x0a'  # "Mom\n" in ASCII as hexadecimal
hexvals

with open('tmp.txt', 'wb') as textfile:
     nbytes = textfile.write(hexvals)

open('tmp.txt', 'wb').write(hexvals)
