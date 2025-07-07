from flask import request, jsonify
from app.review import review_code

def register_review_routes(app):
    @app.route('/review', methods=['POST'])
    def review():
        code = request.json.get("code")
        response = review_code(code)
        return jsonify({'response': response})
