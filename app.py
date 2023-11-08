from flask import Flask, render_template, request, redirect, url_for
from areaofacircle import calculate_circle_area
from areaofatriangle import calculate_triangle_area
from flask import send_file
import csv

app = Flask(__name__, static_url_path='', static_folder='C:\Flask_Intro\static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/triangle')
def triangle():
    return render_template('triangle.html')

@app.route('/circle')
def circle():
    return render_template('circle.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/touppercase', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/circle', methods=['GET', 'POST'])
def areaofacircle():
    area = None
    if request.method == 'POST':
        input_radius = request.form.get('InputFloat', '')
        try:
            input_radius = int(input_radius)
            area = calculate_circle_area(input_radius)
        except ValueError as e:
            area = str(e)
    return render_template('circle.html', area=area)

@app.route('/triangle', methods=['POST'])
def areaofatriangle():
    try:
        input_base = float(request.form.get('InputFloat1', ''))
        input_height = float(request.form.get('InputFloat2', ''))

        area = calculate_triangle_area(input_base, input_height)
    except ValueError as e:
        area = str(e)

    return render_template('triangle.html', area=area)

@app.route('/submit_message', methods=['POST'])
def submit_message():
    if request.method == 'POST':
        name = request.form.get('yourName')
        email = request.form.get('yourEmail')
        subject = request.form.get('subject')
        message = request.form.get('message')
        
        message_data = [name, email, subject, message]
        
        with open('info.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(message_data)
        
        return redirect(url_for('contact'))
    
@app.route('/info.csv')
def info():
    return send_file('info.csv', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
