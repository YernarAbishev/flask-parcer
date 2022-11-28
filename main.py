from flask import Flask
from ktz import  *


app = Flask(__name__)


@app.route("/")
def serverFunction():
    main()
    return "<h1>server started</h1>"


if __name__ == '__main__':
    app.run()