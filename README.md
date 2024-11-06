Network Monitor Web Application
This project is a simple yet effective web-based network monitoring tool designed to check the status of multiple websites in real-time. It allows users to input a list of website URLs, and it will display their status (up/down), ping time, and HTTP status in a table format. The application fetches and displays the status of the websites dynamically, making it easy to monitor their availability and performance.

Features:

Add New Websites: Users can add new websites to the monitoring list.
Website Status Check: Users can check the status of multiple websites by entering their URLs (comma-separated).
Real-time Updates: The status of websites is refreshed every 10 seconds, keeping the information up-to-date.
Table View: The website statuses are displayed in a clean, easy-to-read table with color-coded status indicators:
Green for "Up"
Red for "Down"
Yellow for issues
Gray for errors
Ping Time & HTTP Status: Displays the ping time in milliseconds and the HTTP response status for each website.
Technologies Used:

Frontend: HTML, CSS, JavaScript (Vanilla JS)
Backend: Flask (Python-based web framework)
API: RESTful API to fetch the status of websites
Design: Responsive and user-friendly design with basic styling
Usage Instructions:

Clone the repository to your local machine.
Install the required dependencies for the backend (Flask).
Run the Flask application.
Access the web interface through your browser to monitor websites.
This project is an excellent starting point for building simple monitoring tools and learning about web development, APIs, and network monitoring.
