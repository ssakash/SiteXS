import backend
import xss

#Virtual environment parameters!! (COmmandline arguments)
request_type = backend.argv[1].lower() # GET, POST, PUT
url = backend.argv[2] # URL to be accessed (TODO: remove HTTP specifier and add it inbuilt?)
scanfor = backend.scanner.unset
if len(backend.argv) > 3:
    scanfor = backend.parse_scanner(backend.argv[3]) #Third parameter! what sort of vulnerability to scan for in the site

content = None
x = None

if request_type == 'post':
    x = backend.requests.post(url)
    content = x.text
elif request_type == "get":
    x = backend.requests.get(url)
    content = x.text

elif request_type == "put":
    x = backend.requests.put(url)
    content = x.text

y = backend.requests.head(url)
if (backend.os.path.exists('debug') == False):
    backend.os.mkdir('debug')
htmlfile = open("debug/response_render.html", "w")
textfile = open("debug/response_raw.txt", "w")

textfile.write(content)
htmlfile.write(content)

backend.write_header('HEADER DATA')
for i, j in y.headers.items():
    print(f'{i}: {j}')
backend.end_header

if (scanfor == backend.scanner.XSS):
    backend.write_header('XSS DATA')
    print(xss.scanforxss(content))
    backend.end_header()
