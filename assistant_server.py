from flask import Flask, request, jsonify, Blueprint
import requests, subprocess, os, json
from utils import execute_action



#app = Flask(__name__)

SYSTEM_PROMPT = """You are a local AI assistant that can perform system tasks. 
You have tools: 
- open_app <application> (e.g., SublimeTxT, Safari, Explorer) 
- write_file <filename> <content> 
- web_search <query> (local web search or open browser)

When the user asks something that requires an action, respond in JSON with keys "action" and "target". 
For example, if user says "open browser", output: {"action": "open_app", "target": "Safari"}.
If the request is just asking for information or code, provide the answer with key "message", and optionally include an action if needed.
Never include any external links in the message without user asking. Always respond with a single valid JSON object only.
Do not include comments, explanation, or text before or after the JSON."""



command = Blueprint('command', __name__)

# Example route to handle a command
@command.route('/command', methods=['POST'])
def handle_command():
    print(f"I am in command")

    data = request.get_json(force=True)
    print(f"Data = {data}")
    user_input = data.get('command', '')

    print(f"user_input = {user_input}")
    if not user_input:
        return jsonify({"error": "No command provided"}), 400
    
    # Step 1: Send the user input to the local LLM (via llama.cpp or an API around it)
    llm_response = query_local_llm(user_input)

    print(f"llm_response = {llm_response}")
    # Step 2: Check if LLM wants to perform an action
    action_result = None
    if llm_response.get("action"):
        # If the LLM response is formatted with an action instruction, execute it
        action_result = execute_action(llm_response["action"], llm_response.get("target"))
        print(f"Found action !!!!!")

    # Prepare the final output message
    assistant_reply = llm_response.get("message", "")
    if action_result:
        assistant_reply += f"\n\n(Action result: {action_result})"
    return jsonify({"response": assistant_reply})




def query_local_llm(user_input):
    # Construct payload for Llama.cpp OpenAI-like chat API
    payload = {
        "model": "Llama 3.2 3B Instruct",  # model name can be arbitrary if not required by server
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.7,
        "max_tokens": 2048
    }
    headers = {
        "Content-Type": "application/json"
    }


    print(payload)
    try:
        res = requests.post("http://localhost:4891/v1/chat/completions", json=payload, headers=headers, timeout=60)
        res.raise_for_status()
    except Exception as e:
        print(f"LLM query failed: {e}")
        return {"message": "Sorry, I’m having trouble understanding that."}
    data = res.json()
    print(f"llm response := {data}")


    # Extract assistant's reply text
    assistant_text = data["choices"][0]["message"]["content"]
    print(f"assistant_text = {assistant_text}")
    # Optionally, parse the text if it contains structured action info (we’ll handle next)
    return interpret_llm_output(assistant_text)



def interpret_llm_output(text):
    output = {}
    try:
        parsed = json.loads(text)

        print(f"parser = {parsed}")
        if "action" in parsed:
            print(f"Action is parsed!!")
            output["action"] = parsed["action"]
            output["target"] = parsed.get("target")
            if "message" in parsed:
                output["message"] = parsed["message"]
            else:
                output["message"] = f"Executing {parsed['action']}('{parsed.get('target','')}')"
        else:
            output["message"] = parsed
    except ValueError as e:
        print(f"Caught ValueError: {e}")
        output["message"] = text
    return output