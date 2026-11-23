# blockchain application

import os

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return (render_template("index.html"))

@app.route("/main", methods=["GET", "POST"])
def main():
    return (render_template("main.html"))

@app.route("/transferMoney", methods=["GET", "POST"])
def TransferMoney():
    return (render_template("TransferMoney.html"))


@app.route("/storeMoney")
def store_money():
    return render_template(
        "StoreMoney.html", contract_address=os.getenv("STORE_MONEY_CONTRACT_ADDRESS", "")
    )


if __name__ == "__main__":
    app.run()