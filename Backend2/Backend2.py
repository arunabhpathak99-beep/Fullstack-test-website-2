from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This is our "Storage" for now. 
# It lives in the server's memory.
shared_note = "Welcome to the global notepad! Type something here..."

@app.route('/api/note', methods=['GET', 'POST'])
def manage_note():
    global shared_note # Tells Python to use the variable defined above
    
    # If the website is SENDING us new text (Saving)
    if request.method == 'POST':
        # Get the JSON data sent from the frontend
        data = request.get_json() 
        shared_note = data.get('content', '')
        return jsonify({"message": "Note updated successfully!", "current_note": shared_note})
    
    # If the website is ASKING for the text (Loading)
    if request.method == 'GET':
        return jsonify({"current_note": shared_note})

if __name__ == '__main__':
    app.run()
