from sys import argv
import requests
import os
import pprint #Need to figure out how to use this properly to beautify terminal output

url = argv[2]
request_type = argv[1].lower()
content = None
x = None

if request_type == 'post':
    x = requests.post(url)
    content = x.text
elif request_type == "get":
    x = requests.get(url)
    content = x.text

elif request_type == "put":
    x = requests.put(url)
    content = x.text

y = requests.head(url)
if (os.path.exists('debug') == False):
    os.mkdir('debug')
htmlfile = open("debug/response_render.html", "w")
textfile = open("debug/response_raw.txt", "w")

textfile.write(content)
htmlfile.write(content)
print("==================== HEADER DATA ==============================")
for i, j in y.headers.items():
    print(f'{i}: {j}')
print("=" * 80)

#If you wanna show response body, uncomment
#print(content)