import uuid
from flask import request, jsonify, session, render_template, current_app as app
from .models import ChatMessage
from .chatbot import get_chatbot_response
from . import db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400

    session_id = session.get("session_id", str(uuid.uuid4()))
    session["session_id"] = session_id

    ai_response = get_chatbot_response(user_message)

    chat_message = ChatMessage(session_id=session_id, message=user_message, response=ai_response)
    db.session.add(chat_message)
    db.session.commit()

    return jsonify({"response": ai_response, "status": "success"})

@app.route('/history')
def chat_history():
    if "session_id" not in session:
        return jsonify({"messages": []})

    messages = ChatMessage.query.filter_by(session_id=session["session_id"]).order_by(ChatMessage.timestamp).all()
    history = [{"message": m.message, "response": m.response, "timestamp": m.timestamp.isoformat()} for m in messages]
    return jsonify({"messages": history})

@app.route('/new-session', methods=['POST'])
def new_session():
    session.pop("session_id", None)
    return jsonify({"status": "success", "message": "New session started"})
