from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello world</h1>"