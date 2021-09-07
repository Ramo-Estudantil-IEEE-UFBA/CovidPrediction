from flask import Flask
from dados import todos

app = Flask(__name__)


@app.route("/")
def index():
    exemplo = todos().head(n=10)
    print(exemplo)
    return exemplo.to_html()


if __name__ == "__main__":
    app.run()
