from flask import Flask

def initialize_app():
    application = Flask(__name__)
    application.config['SECRET_KEY'] = "d4d68adfc046579d752916505b72d581"
    
    return application