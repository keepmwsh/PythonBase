from urllib import request
import socks
import socket
import requests

# 不支持链路上存在IPV6的连接
def relyConnect(url):
    s = socks.socksocket()
    # 设置Socks中继
    s.set_proxy(socks.SOCKS5, addr="127.0.0.1", port=1080)
    s.connect(url, 80)
    s.sendall("GET / HTTP/1.1 ...")
    print(s.recv(1024))
    # 关闭Socks中继打开的句柄
    s.close()

# 测试实现了pysocks底层的reuqests请求方式
def relyRequests(url):
    s = socks.socksocket()
    s.set_proxy(socks.SOCKS5, addr="127.0.0.1", port=1080)
    proxys = {
        "http": "socks5://127.0.0.1:1080", "https": "socks5://127.0.0.1:1080"
    }
    relycontent = requests.get(url, proxies=proxys)
    if relycontent.status_code == 200:
        print(relycontent.text)
    else:
        print("Failed...")
    s.close()

# 中继不支持pysocks的第三方模块使用，可通过pysocks的set_default_proxy方法使用
def relyThreePart(url):
    # 设置默认路由
    socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", port=1080)
    socket.socket = socks.socksocket
    content = request.urlopen(url)
    print(content)

if __name__ == "__main__":
    url = "https://www.google.com"
    # relyConnect(url)
    # 中继成功
    relyRequests(url)
    # relyThreePart(url)