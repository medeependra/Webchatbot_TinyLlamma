from flask import Flask, request, render_template, session, redirect, url_for
from LLM_wb import generate_response
import os
from dotenv import load_dotenv
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'fallback-secret-key')  # Use environment variable

# Rate limiting setup
limiter = Limiter(
    app=app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route("/", methods=["GET", "POST"])
@limiter.limit("5 per minute")  # More strict limit on POST requests
def chat():
    if 'history' not in session:
        session['history'] = []

    if request.method == "POST":
        user_input = request.form.get("prompt", "").strip()
        if user_input:  # Only process non-empty inputs
            bot_response = generate_response(user_input)
            session['history'].append({'user': user_input, 'bot': bot_response})
            session.modified = True  # Ensure session is saved
    
    return render_template("chat.html", history=session.get('history', []))

@app.route("/clear", methods=["GET"])
def clear_chat():
    """Clear the chat history"""
    if 'history' in session:
        session.pop('history')
    return redirect(url_for('chat'))

if __name__ == "__main__":
    app.run(debug=os.getenv('FLASK_DEBUG', 'False') == 'True')