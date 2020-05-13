from flask import Flask, Blueprint

# Flask==1.1.2
app = Flask(__name__)

bp1 = Blueprint('bp1', __name__)

@bp1.before_app_request
def bp1_before_app_request():
    """before_app_requestはすべてのリクエストでviewの前に呼ばれる
    """
    print("bp1 before_app_request")

@bp1.before_request
def bp1_before_request():
    """before_requestは対象のBlueprintへルーティングされるリクエストでviewの前に呼ばれる
    """
    print("bp1 before_request")

@bp1.route("/bp1")
def bp1_view():
    print("bp1 view")
    return "/bp1"

bp2 = Blueprint('bp2', __name__)

@bp2.before_app_request
def bp2_before_app_request():
    print("bp2 before_app_request")

@bp2.before_request
def bp2_before_request():
    print("bp2 before_request")

@bp2.route("/bp2")
def bp2_view():
    print("bp2 view")
    return "/bp2"


@app.before_request
def app_before_request1():
    """Flask.before_requestはすべてのリクエストでviewの前に呼ばれる
    """
    print("Flask before_request1")

app.register_blueprint(bp1)
app.register_blueprint(bp2)

@app.before_request
def app_before_request2():
    """登録順で実行されるので、こちらはbp2.before_app_requestよりも後になる
    """
    print("Flask before_request2")

app.run(host="0.0.0.0")
