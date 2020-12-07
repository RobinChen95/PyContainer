from flask import Flask, request
import test
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def rcv_files():
    if request.method == 'GET':   # 如果是 GET 请求方式
        return "You have entered the GEEEEEEEEEEET method!"
    if request.method == 'POST':   # 如果是 POST 请求方式
        file = request.files['file']   # 获取上传的文件
    if file:
        file_path = os.path.join('./rcv_folder', '{}'.format(file.filename))
        file.save(file_path)
        os.system("python "+file_path)
    return "upload success!"


if __name__ == '__main__':
    app.run()
