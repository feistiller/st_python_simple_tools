from flask import Flask, jsonify
import utils
import db
import random
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app, resources=r'/*')


@app.route("/lucky/<lucky_type>")
def get_lucky_user(lucky_type):
    try:
        data = db.get_luck_choice_users()
        choice_num = random.randint(0, len(data) - 1)
        target = data[choice_num]
        print(target)
        db.update_user_lucky(target[0], lucky_type)
        return jsonify(utils.get_json_result(0, target[1], "success"))
    except:
        return jsonify(utils.get_json_result(1, [], "fail"))


@app.route("/get_lucky_user")
def get_all_lucky_user():
    data = db.get_lucky_users()
    return jsonify(utils.get_json_result(0, data, "success"))


if __name__ == '__main__':
    app.run(debug=True, port=5001)
