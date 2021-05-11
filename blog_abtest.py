from flask import Flask, jsonify, request, render_template, make_response
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import CORS
import os

# https 만을 지원하는 기능을 http에서 테스트할 때 필요한 설정
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__, static_url_path='/static')
CORS(app)
app.secure_key = 'seol_server'

login_manager = LoginManager()
login_manager = init_app(app)
login_manager.session_protection = 'strong'

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# login이 안된 사용자가 login이 된 사용자만 접근할 수 있는 api들을 request했을 경우에 에러가나면서 이 함수가 호출이 됨
@login_manager.unauthorized_handler
def unauthorized():
    return make_response(jsonify(success=False), 401)


if __name__ == "__main__":
    app.run(host='localhost', port=8080, debug=True)