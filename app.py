from flask import Flask, render_template, jsonify
from database import get_jobs

app = Flask(__name__)

# jobs = [
#     {
#         'id': 1,
#         'title': 'Data Analyst',
#         'location': 'Kuala Lumpur',
#         'salary': 'RM4000 - 5000'
#     },
#     {
#         'id': 2,
#         'title': 'Software Engineer',
#         'location': 'Penang',
#         'salary': 'RM6000 - 8000'
#     },
#     {
#         'id': 3,
#         'title': 'Marketing Manager',
#         'location': 'Johor Bahru',
#     }
# ]


@app.route("/")
def home():
    jobs = get_jobs()
    return render_template("home.html", jobs=jobs)


@app.route("/api/jobs")
def job_list():
    jobs = get_jobs()
    return jsonify(jobs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

