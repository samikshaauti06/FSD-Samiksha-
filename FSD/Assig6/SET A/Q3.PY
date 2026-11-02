from flask import Flask

app = Flask(__name__)

@app.route("/")
def student_list():
    
    students = ["Sami", "Raja", "Sneha", "Arya", "Priti"]

    sorted_students = sorted(students)

    student_names = "<br>".join(sorted_students)
    
    return f"""
    <h2>List of Students in Alphabetical Order</h2>
    {student_names}
    """

if __name__ == "__main__":
    app.run(debug=True)