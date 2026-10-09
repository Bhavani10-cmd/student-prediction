def get_recommendation(score):

    if score >= 90:
        return """
Excellent Performance!

Recommendations:
✔ Keep maintaining your study routine.
✔ Help other students.
✔ Prepare for competitive exams.
"""

    elif score >= 75:
        return """
Very Good Performance!

Recommendations:
✔ Increase revision time.
✔ Practice previous papers.
✔ Improve problem solving.
"""

    elif score >= 60:
        return """
Good Performance

Recommendations:
✔ Study at least 2 extra hours.
✔ Improve attendance.
✔ Revise weak subjects.
"""

    else:
        return """
Needs Improvement

Recommendations:
✔ Meet your teacher.
✔ Follow a daily study plan.
✔ Complete all assignments.
✔ Increase study hours.
"""