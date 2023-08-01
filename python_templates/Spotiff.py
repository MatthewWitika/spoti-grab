from flask import Flask, request, redirect, render_template_string
from dotenv import load_dotenv
import os
import tkinter as tk
from tkinter import ttk
import webbrowser

app = Flask(__name__)

load_dotenv()

# Replace 'YOUR_CLIENT_ID' with your actual Spotify client ID
# This is the same client ID you used to obtain the access token or authorization code
client_id = os.getenv('CLIENT_ID')

# Replace 'YOUR_REDIRECT_URI' with the URI you want to use as your redirect_uri
# This URI should be a valid URL where Spotify will redirect the user after login and authorization
redirect_uri = 'https://localhost:5000'

@app.route('/')
def index():
     # Use a template to render the home page with centered elements and input fields
    template =  """
    <html>
    <head>
        <style>
            body, html {
                height: 100%;
                display: flex;
                justify-content: center;
                align-items: center;
            }
            .center-content {
                text-align: center;
            }
            .input-field {
                padding: 5px;
                font-size: 16px;
            }
            .submit-button {
                padding: 10px 20px;
                font-size: 18px;
                background-color: #1db954;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .spotify-login-link {
                text-decoration: none;
                color: white;
            }
            .spotify-login-button {
                padding: 10px 20px;
                font-size: 18px;
                background-color: #1db954;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class="center-content">
            <h1>Spoti-snatch App</h1>
            <form action="/">
                <input class="input-field" type="text" name="input_text" placeholder="Enter text">
                <button class="submit-button" type="submit">Submit</button>
            </form>
            <br>
            <a class="spotify-login-link" href="{{ spotify_login_url }}">
                <button class="spotify-login-button">Login to Spotify</button>
            </a>
        </div>
    </body>
    </html>
    """
    spotify_login_url = f"https://accounts.spotify.com/authorize?client_id={client_id}&response_type=code&redirect_uri=https://localhost:5000/spotify_callback"
    return render_template_string(template,spotify_login_url=spotify_login_url)

@app.route('/spotify_callback')
def spotify_callback():
    # After a user logs in and grants permission, Spotify will redirect them to this endpoint with an authorization code
    # The authorization code will be present in the 'code' query parameter of the request
    code = request.args.get('code')
    
    # You can handle the authorization code here (e.g., exchange it for an access token or use it in the "Authorization Code" flow)
    
    return f'This is the Spotify callback page. Authorization code: {code}'




if __name__ == '__main__':
    app.run()
