Readme



##################
## Queries to llm
#################



curl -X POST http://localhost:4891/v1/chat/completions -d '{
"model": "Llama 3.2 1B Instruct",
"messages": [{"role":"user","content":"Who is Lionel Messi?"}],
"max_tokens": 50,
"temperature": 0.28
}'


curl -X POST http://localhost:4891/v1/chat/completions -d '{
"model": "Llama 3.2 1B Instruct",
"messages": [{
  "role": "system",
  "content": "You are a local AI assistant that can perform system tasks. You have tools: - open_app <application> (e.g., SublimeTxT, Safari, Explorer) - write_file <filename> <content> - web_search <query> (local web search or open browser) When the user asks something that requires an action, respond in JSON with keys \"action\" and \"target\". For example, if user says \"open Google\", output: {\"action\": \"open_app\", \"target\": \"Safari\"}. If the request is just asking for information or code, provide the answer with key \"message\", and optionally include an action if needed. Never include any external links in the message without user asking."
}
, {"role":"user","content":"what is 2+2"}],
"max_tokens": 50,
"temperature": 0.28
}'



curl -X POST http://localhost:4891/v1/chat/completions -d '{
  "model": "Llama 3.2 3B Instruct",
  "messages": [
    {
      "role": "system",
      "content": "You are a local AI assistant that can perform system tasks. \nYou have tools: \n- open_app <application> (e.g., SublimeTxT, Safari, Explorer) \n- write_file <filename> <content> \n- web_search <query> (local web search or open browser)\n\nWhen the user asks something that requires an action, respond in JSON with keys \"action\" and \"target\". \nFor example, if user says \"open Google\", output: {\"action\": \"open_app\", \"target\": \"Safari\"}.\nIf the request is just asking for information or code, provide the answer with key \"message\", and optionally include an action if needed.\nNever include any external links in the message without user asking."
    },
    {
      "role": "user",
      "content": "what is 2+2"
    }
  ],
  "temperature": 0.5
}'


Action curl


curl -X POST http://localhost:4891/v1/chat/completions -d '{
  "model": "Llama 3.2 3B Instruct",
  "messages": [
    {
      "role": "system",
      "content": "You are a local AI assistant that can perform system tasks. \nYou have tools: \n- open_app <application> (e.g., SublimeTxT, Safari, Explorer) \n- write_file <filename> <content> \n- web_search <query> (local web search or open browser)\n\nWhen the user asks something that requires an action, respond in JSON with keys \"action\" and \"target\". \nFor example, if user says \"open Google\", output: {\"action\": \"open_app\", \"target\": \"Safari\"}.\nIf the request is just asking for information or code, provide the answer with key \"message\", and optionally include an action if needed.\nNever include any external links in the message without user asking. Always respond with a single valid JSON object only. Do not include comments, explanation, or text before or after the JSON."
    },
    {
      "role": "user",
      "content": "open browser"
    }
  ],
  "temperature": 0.7
}'


curl -X POST http://localhost:4891/v1/chat/completions -d '{
  "model": "Llama 3.2 3B Instruct",
  "messages": [
    {
      "role": "system",
      "content": "You are a local AI assistant that can perform system tasks. \nYou have tools: \n- open_app <application> (e.g., SublimeTxT, Safari, Explorer) \n- write_file <filename> <content> \n- web_search <query> (local web search or open browser)\n\nWhen the user asks something that requires an action, respond in JSON with keys \"action\" and \"target\". \nFor example, if user says \"open Google\", output: {\"action\": \"open_app\", \"target\": \"Safari\"}.\nIf the request is just asking for information or code, provide the answer with key \"message\", and optionally include an action if needed.\nNever include any external links in the message without user asking. Always respond with a single valid JSON object only. Do not include comments, explanation, or text before or after the JSON."
    },
    {
      "role": "user",
      "content": "Help me write a hello world program in Python"
    }
  ],
  "temperature": 0.7,
  "max_tokens": 2048
}'


##########################
## Queries to Server
###########################


curl -X POST http://127.0.0.1:5000/command -d '{
"command":"what is 2+2"
}'