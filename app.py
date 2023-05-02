from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Kuala Lumpur',
        'salary': 'RM4000 - 5000'
    },
    {
        'id': 2,
        'title': 'Software Engineer',
        'location': 'Penang',
        'salary': 'RM6000 - 8000'
    },
    {
        'id': 3,
        'title': 'Marketing Manager',
        'location': 'Johor Bahru',
    },
    {
        'id': 4,
        'title': 'Graphic Designer',
        'location': 'Kuala Lumpur',
        'salary': 'RM3000 - 4000'
    },
    {
        'id': 5,
        'title': 'Human Resources Coordinator',
        'location': 'Petaling Jaya',
        'salary': 'RM4000 - 5000'
    },
    {
        'id': 6,
        'title': 'Sales Executive',
        'location': 'Melaka',
        'salary': 'RM3500 - 4500'
    },
    {
        'id': 7,
        'title': 'Data Scientist',
        'location': 'Kuala Lumpur',
        'salary': 'RM9000 - 12000'
    },
    {
        'id': 8,
        'title': 'Customer Service Representative',
        'location': 'Ipoh',
        'salary': 'RM2500 - 3000'
    },
    {
        'id': 9,
        'title': 'Operations Manager',
        'location': 'Kuching',
        'salary': 'RM10000 - 12000'
    },
    {
        'id': 10,
        'title': 'Content Writer',
        'location': 'Subang Jaya',
        'salary': 'RM4000 - 5000'
    },
    {
        'id': 11,
        'title': 'Financial Analyst',
        'location': 'Kuala Lumpur',
        'salary': 'RM7000 - 9000'
    }
]

@app.route("/")
def home():
    return render_template("home.html", jobs=jobs)


@app.route("/jobs")
def job_list():
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

