import webbrowser
import subprocess

def execute_action(action, target=None):
    action = action.lower()
    try:
        if action == "open_app":
            return open_application(target)
        elif action == "open_url":
            if target:
                webbrowser.open(target)  # opens URL in default browser
                return f"Opened URL: {target}"
        elif action == "open_file":
            if target:
                os.startfile(target)  # Windows: open file/folder with default program
                return f"Opened file/folder: {target}"
        elif action == "write_file":
            if target:
                filename, content = target.split("|||", 1)
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(content)
                return f"Wrote to file: {filename}"
        else:
            return f"Unknown action: {action}"
    except Exception as e:
        return f"Error executing {action}: {str(e)}"

def open_application(app_name):
    if not app_name:
        return "No application specified."
    app = app_name.lower()
    if app in ("sublime", "sublime text", "code"):
        subprocess.Popen(["SublimeTxT"])  
        return "SublimeTxT launched."
    elif app in ("safari", "browser"):
        subprocess.Popen(["open", "-a", "Safari", "https://www.google.com"])
        return "Safari opened."
    elif app in ("finder", "file explorer"):
        subprocess.Popen(["finder"])
        return "File Explorer opened."
    else:
        return f"Don't know how to open '{app_name}'."