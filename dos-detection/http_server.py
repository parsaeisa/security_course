from http.server import BaseHTTPRequestHandler, HTTPServer
import csv
from ipaddress import ip_address
import pandas as pd
from block_ips import get_malware_ips
from datetime import datetime

hostName = "localhost"
serverPort = 8080

with open('request_logger.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['IP', 'time'])

class MyHandler(BaseHTTPRequestHandler):
    def setup(self) -> None:
        return super().setup()

    def do_GET(self):
        ip_addr = str(self.client_address[0])
        row = [ip_addr, datetime.now()]

        malware_ips = get_malware_ips()
        if ip_addr in malware_ips : 
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>You are dos attack</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))   

        else :
            df = pd.read_csv('request_logger.csv')
            df.loc[df.shape[0]] = row
            df.to_csv('request_logger.csv', index=False)

            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            
            self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
            self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<body>", "utf-8"))
            self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
            self.wfile.write(bytes("<p>" + self.client_address[0] + "</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))        


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyHandler)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()

    print("Server stopped.")
