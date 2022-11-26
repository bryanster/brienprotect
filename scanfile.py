import clamd

cd = clamd.ClamdNetworkSocket(host="127.0.0.1" , port=3311, timeout=None)

print(cd.scan("C:\\Users\\bryan\\Downloads\\python-3.11.0-amd64.exe"))