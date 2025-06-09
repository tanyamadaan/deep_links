from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect_app_installation', methods=['GET'])
def detect_app_installation():
    # Example logic to detect app installation based on user-agent header
    user_agent = request.headers.get('User-Agent', '')
    is_app_installed = False

    # Example: Check if the user-agent contains a string specific to your app
    # if 'Magicpin' in user_agent:
    #     is_app_installed = True

    return jsonify({'header': request.headers})

if __name__ == '__main__':
    app.run(debug=True)