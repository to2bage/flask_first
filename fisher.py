from flask import Flask

from app import create_app

app = create_app()


if __name__ == '__main__':
    # Threaded mode is enabled by default.
    # app.run(debug=app.config["DEBUG"], host="0.0.0.0")
    # 开启多线程
    app.run(debug=app.config["DEBUG"], host="0.0.0.0", threaded=True)


"""
http://127.0.0.1:5000/book/search?q=9787501524044&page=1
http://127.0.0.1:5000/book/search?q=霍金&page=1
"""