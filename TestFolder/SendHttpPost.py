# 构造Http请求转发文件
import requests


url = " http://127.0.0.1:5000/"
file_name = "query.py"
file = open("./"+file_name, 'rb')
files = {'file': file}
response = requests.post(url, files=files)
file.close()
print(response.content)
