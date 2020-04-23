import random
from flask import Blueprint
from flask import jsonify
from flask import request
from flasgger.utils import swag_from 
from src import __version__

"REF : http://brunorocha.org/python/flask/flasgger-api-playground-with-flask-and-swagger-ui.html"

testpage = Blueprint('testpage',__name__)

@testpage.route('/')
@testpage.route('/api')
@testpage.route('/api/testpage')
@swag_from('flasgger\\homepage.yml') 
def homepage():
    return("testpage")

@testpage.route('/termsofservice') 
def termsofservice():
    return("there is no terms of service for this api for now")

@testpage.route('/api/version')
@testpage.route('/version')
def get_api_version():
  return __version__

@testpage.route('/api/language/<string:language>/', methods=['GET'])
def index(language):
    """
    This is the test language awesomeness API
    Call this api passing a language name and get back its features
    ---
    tags:
      - Test Language API
    parameters:
      - name: language
        in: path
        type: string
        required: true
        description: The language name
      - name: size
        in: query
        type: integer
        description: size of awesomeness
    responses:
      500:
        description: Error The language is not awesome!
      200:
        description: A language with its awesomeness
        schema:
          id: awesome
          properties:
            language:
              type: string
              description: The language name
              default: Lua
            features:
              type: array
              description: The awesomeness list
              items:
                type: string
              default: ["perfect", "simple", "lovely"]

    """

    language = language.lower().strip()
    features = [
        "awesome", "great", "dynamic", 
        "simple", "powerful", "amazing", 
        "perfect", "beauty", "lovely"
    ]
    size = int(request.args.get('size', 1))
    if size > 9:
        return "An error occurred, invalid size for awesomeness", 500
    if language in ['php', 'vb', 'visualbasic', 'actionscript']:
        return "An error occurred, invalid language for awesomeness", 500
    return jsonify(
        language=language,
        features=random.sample(features, size)
    )
