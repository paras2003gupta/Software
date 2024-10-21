
# COCOMO Cost Estimation Web Application

This project is a simple web application that estimates software project costs using the **COCOMO (Constructive Cost Model)**. Users can input project parameters (model type and KLOC), and the application calculates effort, development time, average staff size, and productivity.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Screenshots](#screenshots)
- [License](#license)

## Features

- Choose from **Organic**, **Semidetached**, or **Embedded** COCOMO models.
- Enter project size in KLOC (Thousands of Lines of Code).
- Calculate key metrics like:
  - Effort (in person-months)
  - Development time (in months)
  - Average staff size
  - Productivity
- Responsive and modern UI with gradient backgrounds and hover animations.
- Simple, intuitive, and easy-to-use interface.

## Technologies Used

- **HTML5** for structure.
- **CSS3** for styling and hover effects.
- **Python (Flask)** for the backend logic and calculations.
- **COCOMO formula** for effort and development cost estimation.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/cocomo-calculator.git
   cd cocomo-calculator
   ```

2. **Install dependencies**:
   Make sure you have Python 3 installed. Then install the necessary Python packages:
   ```bash
   pip install flask
   ```

3. **Run the Flask app**:
   ```bash
   python app.py
   ```

4. **Access the web application**:
   Open your web browser and go to:
   ```
   http://127.0.0.1:5000/
   ```

## Usage

1. Open the application in your browser.
2. Select the type of **COCOMO Model** from the dropdown:
   - Organic
   - Semidetached
   - Embedded
3. Enter the **KLOC** (Project Size in Thousands of Lines of Code).
4. Click **Calculate Cost**.
5. View the results including:
   - Effort (person-months)
   - Development time (months)
   - Average staff size (persons)
   - Productivity (KLOC/person-month)

## File Structure

```
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
```

## Screenshots

### Homepage (COCOMO Input)
![COCOMO Input Page](screenshots/homepage.png)

### Results Page (COCOMO Results)
![COCOMO Results Page](screenshots/results.png)

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
