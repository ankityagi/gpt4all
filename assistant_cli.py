import requests, sys


if __name__ == "__main__":
    base_url = "http://127.0.0.1:5000"  # Flask server URL
    print("Local AI Assistant CLI. Type a command (or 'exit'):")
    while True:
        user_cmd = input("> ")
        if user_cmd.lower() in ["exit", "quit"]:
            break
        try:
            resp = requests.post(f"{base_url}/command", json={"command": user_cmd})
            data = resp.json()
            if "response" in data:
                print(data["response"])
            else:
                print(f"Error: {data.get('error', resp.status_code)}")
        except Exception as e:
            print(f"Failed to connect to assistant: {e}")
            sys.exit(1)