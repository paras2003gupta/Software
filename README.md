This project is a simple web application that estimates software project costs using the COCOMO (Constructive Cost Model). Users can input project parameters (model type and KLOC), and the application calculates effort, development time, average staff size, and productivity.

Table of Contents
Features
Technologies Used
Installation
Usage
File Structure
Screenshots
License
Features
Choose from Organic, Semidetached, or Embedded COCOMO models.
Enter project size in KLOC (Thousands of Lines of Code).
Calculate key metrics like:
Effort (in person-months)
Development time (in months)
Average staff size
Productivity
Responsive and modern UI with gradient backgrounds and hover animations.
Simple, intuitive, and easy-to-use interface.
Technologies Used
HTML5 for structure.
CSS3 for styling and hover effects.
Python (Flask) for the backend logic and calculations.
COCOMO formula for effort and development cost estimation.
Installation
To run this project locally, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/cocomo-calculator.git
cd cocomo-calculator
Install dependencies: Make sure you have Python 3 installed. Then install the necessary Python packages:

bash
Copy code
pip install flask
Run the Flask app:

bash
Copy code
python app.py
Access the web application: Open your web browser and go to:

arduino
Copy code
http://127.0.0.1:5000/
Usage
Open the application in your browser.
Select the type of COCOMO Model from the dropdown:
Organic
Semidetached
Embedded
Enter the KLOC (Project Size in Thousands of Lines of Code).
Click Calculate Cost.
View the results including:
Effort (person-months)
Development time (months)
Average staff size (persons)
Productivity (KLOC/person-month)
File Structure
graphql
Copy code
.
├── app.py              # Main Python file running the Flask web server
├── templates/
│   ├── index.html      # Homepage HTML file with a form for input
│   ├── result.html     # HTML file to display the result
├── static/
│   ├── css/
│   │   ├── result.css  # Additional CSS for results page (optional, inline CSS also used)
├── README.md           # Project documentation
└── requirements.txt    # Python dependencies
Screenshots
Homepage (COCOMO Input)

Results Page (COCOMO Results)

License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to adjust any links or sections as needed (e.g., adding your GitHub repository, screenshots, etc.).
