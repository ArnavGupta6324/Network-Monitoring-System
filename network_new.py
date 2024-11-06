import os
import requests
from flask import Flask, jsonify, render_template, request, redirect, url_for

app = Flask(__name__)

# Predefined list of websites to monitor (can be expanded or modified)
default_websites = [
    "google.com",
    "youtube.com",
    "facebook.com",
    "twitter.com",
    "instagram.com",
    "linkedin.com",
    "reddit.com",
    "amazon.com",
    "microsoft.com",
    "apple.com"
]

pause = 10  # Pause in seconds between checks

def get_ping_time(url):
    """
    Function to perform a ping test to measure round-trip time to a given URL.
    Uses the 'ping' command line tool in Windows.
    """
    ping_command = f"ping -n 1 {url}"  # Construct ping command for Windows
    ping_response = os.popen(ping_command).read()  # Execute ping command and read response
    ping_time = None

    if "Received = 1" in ping_response:
        # If a response is received, parse the ping time from the output
        for line in ping_response.splitlines():
            if "time=" in line.lower():
                ping_time = line.split("time=")[1].split(" ")[0]
                break

    return ping_time if ping_time else "N/A"

def get_http_status(url):
    """
    Function to perform an HTTP GET request to a given URL and return the status code.
    """
    try:
        http_response = requests.get(f"http://{url}")  # Send GET request to URL
        return http_response.status_code  # Return HTTP status code
    except requests.exceptions.RequestException:
        return "Error"  # Return 'Error' if request encounters an exception

@app.route('/')
def index():
    """
    Route to render the index.html template.
    """
    return render_template('index.html')

@app.route('/status', methods=['GET'])
def status():
    """
    Route to fetch the status of websites.
    Combines predefined websites with user-input websites and returns JSON response.
    """
    # Combine predefined websites with user-input websites from query parameters
    websites = default_websites + request.args.getlist('website')
    results = []

    # Iterate over combined list of websites
    for url in websites:
        ping_time = get_ping_time(url)  # Get ping time for the website
        http_status = get_http_status(url)  # Get HTTP status code for the website

        # Determine status class based on ping time and HTTP status
        status_class = "up"
        if ping_time == "N/A" or http_status == "Error":
            status_class = "issue"
        elif http_status != 200:
            status_class = "down"

        # Append website status information to results list
        results.append({
            "url": url,
            "status_class": status_class,
            "ping_time": ping_time,
            "http_status": http_status
        })
    
    return jsonify(results)  # Return results as JSON response

@app.route('/add_website', methods=['POST'])
def add_website():
    """
    Route to add a new website to the monitoring list.
    Expects a JSON body with 'website' key.
    """
    new_website = request.json.get('website')
    
    if new_website:
        if new_website not in default_websites:
            default_websites.append(new_website)
            return jsonify({"message": "Website added successfully!", "websites": default_websites}), 200
        else:
            return jsonify({"message": "Website already in the list."}), 400
    return jsonify({"message": "No website provided."}), 400

if __name__ == "__main__":
    app.run(debug=True)
