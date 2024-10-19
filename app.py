from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# COCOMO parameters for different project types
COCOMO_PARAMS = {
    "Organic": {"a_b": 2.4, "b_b": 1.05, "c_b": 2.5, "d_b": 0.38},
    "Semidetached": {"a_b": 3.0, "b_b": 1.12, "c_b": 2.5, "d_b": 0.35},
    "Embedded": {"a_b": 3.6, "b_b": 1.20, "c_b": 2.5, "d_b": 0.32}
}

# Function to calculate COCOMO
def calculate_cocomo(model_type, kloc):
    if model_type not in COCOMO_PARAMS:
        return "Invalid project type"
    
    params = COCOMO_PARAMS[model_type]
    effort = params['a_b'] * (kloc ** params['b_b'])  # Effort in person-months
    dev_time = params['c_b'] * (effort ** params['d_b'])  # Development time in months
    avg_staff_size = effort / dev_time  # Average staff size
    productivity = kloc / effort  # Productivity
    return effort, dev_time, avg_staff_size, productivity

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling form submission
@app.route('/calculate', methods=['POST'])
def calculate():
    model_type = request.form['model_type']
    kloc = float(request.form['kloc'])
    effort, dev_time, avg_staff_size, productivity = calculate_cocomo(model_type, kloc)
    
    return render_template('result.html', model_type=model_type, kloc=kloc, 
                           effort=effort, dev_time=dev_time, 
                           avg_staff_size=avg_staff_size, productivity=productivity)

if __name__ == '__main__':
    app.run(debug=True)
