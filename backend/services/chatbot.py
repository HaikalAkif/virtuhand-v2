from flask import Blueprint, request, jsonify
from services.chatbot import get_chatbot_response

chatbot_bp = Blueprint("chatbot", __name__)

@chatbot_bp.route("/", methods=["POST"])
def chatbot():
    data = request.json
    user_query = data.get("query", "")
    response = get_chatbot_response(user_query)
    return jsonify({"response": response})
