from flask import Flask, request
from random import choice
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# decorator with path and post
# handler takes in post, looks for key words, passes to some caching method
# store in cache
# return Id

users = {}
rid = 1

@app.route("/create_user", methods=["POST"])
def handle_create_request():
  user_name = request.form['user_name']
  password = request.form['password']
  rid = add_user(user_name, password)
  return str(rid)

def add_user(user_name, password):
  global rid
  users[rid] = [user_name, password]
  tmp = rid
  rid += 1
  return tmp


@app.route("/add_credit_card", methods=["POST"])
def handle_add_credit():
  exp_month = request.form['exp_month']
  exp_year = request.form['exp_year']
  cvc = request.form['cvc']
  card_num = request.form['card_number']
  card = {
    'exp_month': exp_month,
    'exp_year': exp_year,
    'cvc': cvc,
    'number': card_num
  }
  rid = request.form['rid']
  token = add_card(rid, card)

def add_card(rid, card):
  obj = {'type':'card', 'card':card}
  url = 'https://api.stripe.com/v1/payment_methods'
  req = requests.post(url, auth=('sk_test_51J09wlGVUCKboX73586nOg6UyifeQhRE4OO3FfpicW8p2yHLduTHxH7y0ipGFLGEDeUUQ2fahOaCvAi4Fr8sEzvY00uWqYuheb', ''), data=obj)



