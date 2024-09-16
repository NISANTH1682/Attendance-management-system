from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Sample data
students = ["Nisanth", "Nandhini", "Sanjeeve", "Deebhika", "Nithiya", "Jega"]
subjects = ["Python", "JAVA", "C/C++", "Designing", "Networks", "Kotlin"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Initialize attendance count for each subject
        attendance_count = {subject: {'present': 0, 'absent': 0, 'absent_students': []} for subject in subjects}

        # Process each student's attendance for each subject
        for student in students:
            for subject in subjects:
                # Check if the present checkbox is checked
                if request.form.get(f"{student}_{subject}_present"):
                    attendance_count[subject]['present'] += 1
                # Check if the absent checkbox is checked
                elif request.form.get(f"{student}_{subject}_absent"):
                    attendance_count[subject]['absent'] += 1
                    attendance_count[subject]['absent_students'].append(student)

        # Calculate total counts for all subjects
        total_present = sum(count['present'] for count in attendance_count.values())
        total_absent = sum(count['absent'] for count in attendance_count.values())

        # Add totals to the attendance_count dictionary
        attendance_count['total'] = {'present': total_present, 'absent': total_absent}

        return render_template('result.html', attendance=attendance_count)

    # Render the form page with current date
    return render_template('index.html', students=students, subjects=subjects, date=datetime.now().strftime("%Y-%m-%d"))

if __name__ == '__main__':
    app.run(debug=True)
