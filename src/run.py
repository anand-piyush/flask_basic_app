
from flask import Flask
from flasgger import Swagger
from src.views.testpage import testpage

app = Flask(__name__)
app.register_blueprint(testpage)
'''
CSS MODIFICATIONS IS ALSO AN OPTION TO TRY (not tried these but the coded ones in the file)
swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['swagger_ui_css'] = 'my_css.css'
Swagger(app, config=swagger_config)

Similarly footer can be removed by manipulating following file manually
D:\\PythonApps\\flask_app_iis\\env\\Lib\\site-packages\\flasgger\\ui3\\templates\\flasgger\\footer.html
'''
app.config['SWAGGER'] = {
    'title': 'Sample API',
    'version': '2.0.1',
    'uiversion': 3, # for older versions set a lesser value as we have used 2 in my previous company
    "specs_route": "/api/doc/",
    'description' : 'Coded by Piyush Anand',
    'termsOfService' : '/termsofservice'
}
swag = Swagger(app)

if __name__ == "__main__":
    app.run('0.0.0.0')