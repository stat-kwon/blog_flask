from flask import Flask, Blueprint, request, render_template, make_response, jsonify
from werkzeug.utils import redirect

blog_abtest = Blueprint('blog', __name__)

@blog_abtest.route('/set_email', methods=['POST'])
    
@blog_abtest.route('/test_blog')
def test_blog():
    return render_template('blog_A.html')