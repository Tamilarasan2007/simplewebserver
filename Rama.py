from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head></head>
    <title>Tamilarasan-25009942</title>
    <body>
        <center>
        <h1>DEVICE SPECIFICATION- 25009942</h1>
        <hr size="10">
        
        <table border="1" cellpadding="10">

            <tr>
                
                </tr>
                    <th>Processor</th><th>Ram</th><th>SSD</th>
                </tr>
                <tr>
                    <td>intel i3 1202u</td><td>8gb</td><td>512gb</td>
                </tr>
        </table>
        </center>
        <hr>
    </body>



</html>

"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()