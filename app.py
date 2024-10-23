from flask import Flask
from zeroshot import zeroshot_bp
from firstshot import firstshot_bp
from personalshot import personalshot_bp

app = Flask(__name__)

# Registering blueprints
app.register_blueprint(zeroshot_bp)
app.register_blueprint(firstshot_bp)
app.register_blueprint(personalshot_bp)

if __name__ == '__main__':
    app.run(debug=True)

#     test




#
# from flask import Flask, request, jsonify
# import base64
#
# app = Flask(__name__)
#
# # Hardcoded username and password for authentication
# USERNAME = "my_user"
# PASSWORD = "my_password"
#
# # @app.route('/', methods=['GET'])
# # def home():
# #     return '<p>Hello world</p>'
#
# # Route to receive JSON and process it after authentication
# @app.route('/process', methods=['POST'])
# def process_request():
#     # Get the authorization header
#     auth_header = request.headers.get('Authorization')
#
#     # Check if the header contains valid credentials
#     if not auth_header or not check_credentials(auth_header):
#         return jsonify({"message": "Unauthorized"}), 401
#
#     # Get the JSON data from the request body
#     data = request.get_json()
#
#     # Dummy processing: Analyze and return a response
#     result = analyze_data(data)
#     return jsonify(result), 200
#
#
# # Function to check if the Authorization header contains valid credentials
# def check_credentials(auth_header):
#     if auth_header.startswith("Basic "):
#         # Extract and decode the base64-encoded username:password
#         auth_value = auth_header.split(" ")[1]
#         decoded_value = base64.b64decode(auth_value).decode('utf-8')
#         username, password = decoded_value.split(":")
#
#         # Check if the username and password match
#         return username == USERNAME and password == PASSWORD
#     return False
#
#
# # Dummy function to simulate analysis of the received data
# def analyze_data(data):
#     # Example: You can modify this to perform any logic
#     return {
#         "status": "success",
#         "received": data,
#         "message": "Data processed successfully"
#     }
#
#
# if __name__ == '__main__':
#     app.run(debug=True)

