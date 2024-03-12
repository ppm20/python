from flask import Flask, jsonify, request
 
app = Flask(__name__)
 
# Dummy data to store POSTed information
stored_data = {}
 
@app.route('/post', methods=['POST'])
def post_data():
    data = request.get_json()
    # Assuming the data has a key called 'message'
    message = data.get('message', '')
    stored_data['message'] = message
    return jsonify({'success': True})
 
@app.route('/get', methods=['GET'])
def get_data():
    return jsonify(stored_data)
 
if __name__ == '__main__':
    app.run(debug=True)