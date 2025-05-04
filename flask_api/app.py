from flask import Flask
from flask_restful import Api
from resources.post import PostAPI

app = Flask(__name__)
api = Api(app)

api.add_resource(PostAPI, '/api/posts')

if __name__ == '__main__':
    app.run(debug=True)
