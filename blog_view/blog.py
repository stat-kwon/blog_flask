from flask import Flask, Blueprint, request, render_template, make_response, jsonify
from werkzeug.utils import redirect

blog_abtest = Blueprint('blog', __name__)

@blog_abtest.route('/set_email', methods=['POST'])
def set_email():
    if request.method == 'GET':
        print('set_email',request.args.get('user_email'))
        return redirect('/blog/test_blog')
    else:
        print('set_email', request.headers)
        print('set_email', request.get_json())
        return redirect('/blog/test_blog')
    
@blog_abtest.route('/test_blog')
def test_blog():
    return render_template('blog_A.html')