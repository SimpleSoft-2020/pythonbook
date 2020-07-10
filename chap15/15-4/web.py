import http.server
import socketserver
#端口号
PORT = 9000
server = ('',PORT)
#HTTP请求处理器
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(server, Handler);
print("启动网页服务成功，端口号为：", PORT)
httpd.serve_forever()
