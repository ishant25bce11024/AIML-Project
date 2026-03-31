from flask import Flask, request, render_template_string
import pandas as pd
from datetime import datetime
import webbrowser, threading

app = Flask(__name__)

# ================= ML LOGIC =================
def generate_schedule(subjects, deadlines, weakness, total_hours):
    df = pd.DataFrame({
        'subject': subjects,
        'deadline': deadlines,
        'weakness': weakness
    })

    today = datetime.today()

    df['deadline'] = pd.to_datetime(df['deadline'])
    df['weakness'] = df['weakness'].astype(int)
    df['days_left'] = (df['deadline'] - today).dt.days

    df['priority'] = (df['weakness'] * 2) + (10 / (df['days_left'] + 1))
    df = df.sort_values(by='priority', ascending=False)

    total_priority = df['priority'].sum()
    df['hours'] = (df['priority'] / total_priority) * total_hours

    plan = []
    day = 1
    for _, row in df.iterrows():
        plan.append({
            'day': f"Day {day}",
            'subject': row['subject'],
            'hours': round(row['hours'], 2)
        })
        day += 1

    return plan


# ================= UI =================
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Smart Study Planner</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

<style>
body {
    font-family: Arial;
    background: #0a0a0a;
    color: #00ffcc;
}

.container {
    max-width: 900px;
    margin: auto;
    padding: 20px;
}

input {
    padding: 10px;
    margin: 5px;
    background: black;
    color: #00ffcc;
    border: 1px solid #00ffcc;
}

button {
    padding: 10px;
    margin: 5px;
    background: #00ffcc;
    border: none;
    color: black;
    cursor: pointer;
}

table {
    width: 100%;
    margin-top: 20px;
    border-collapse: collapse;
}

td, th {
    border: 1px solid #00ffcc;
    padding: 10px;
    text-align: center;
}

h1, h2 {
    text-align: center;
}
</style>
</head>

<body>

<div class="container">
<h1>⚡ Smart Study Planner</h1>

<form method="POST">

<h3>Total Study Hours</h3>
<input type="number" name="total_hours" required>

<h3>Subjects</h3>
<div id="inputs">
    <div>
        <input name="subject" placeholder="Subject" required>
        <input type="date" name="deadline" required>
        <input type="number" name="weakness" placeholder="Weakness (1-5)" required>
    </div>
</div>

<button type="button" onclick="addRow()">+ Add Subject</button>

<h3>📅 Timetable</h3>
<input name="timetable" placeholder="e.g. 6-8 Math, 8-9 Break..." style="width:100%">

<h3>📊 Productivity Inputs</h3>
<input type="number" name="used_hours" placeholder="Used Hours">
<input type="number" name="wasted_hours" placeholder="Wasted Hours">

<br><br>

<!-- SEPARATE BUTTONS -->
<button name="action" value="plan">Generate Study Plan</button>
<button name="action" value="timetable">Show Timetable</button>
<button name="action" value="productivity">Show Productivity</button>

</form>

{% if schedule %}
<h2>📚 Study Plan</h2>
<table>
<tr><th>Day</th><th>Subject</th><th>Hours</th></tr>
{% for item in schedule %}
<tr>
<td>{{item.day}}</td>
<td>{{item.subject}}</td>
<td>{{item.hours}}</td>
</tr>
{% endfor %}
</table>
{% endif %}

{% if timetable %}
<h2>🕒 Your Timetable</h2>
<p>{{timetable}}</p>
{% endif %}

{% if used is not none %}
<h2>📊 Productivity</h2>
<canvas id="chart"></canvas>

<script>
var ctx = document.getElementById('chart').getContext('2d');

new Chart(ctx, {
    type: 'pie',
    data: {
        labels: ['Used Hours', 'Wasted Hours'],
        datasets: [{
            data: [{{used}}, {{wasted}}],
        }]
    }
});
</script>
{% endif %}

</div>

<script>
function addRow() {
    let div = document.createElement('div');
    div.innerHTML = `
        <input name="subject" placeholder="Subject" required>
        <input type="date" name="deadline" required>
        <input type="number" name="weakness" placeholder="Weakness (1-5)" required>
    `;
    document.getElementById('inputs').appendChild(div);
}
</script>

</body>
</html>
"""

# ================= ROUTE =================
@app.route('/', methods=['GET', 'POST'])
def home():
    schedule = None
    timetable = None
    used = None
    wasted = None

    if request.method == 'POST':
        action = request.form.get('action')

        subjects = request.form.getlist('subject')
        deadlines = request.form.getlist('deadline')
        weakness = request.form.getlist('weakness')
        total_hours = float(request.form.get('total_hours', 0))

        if action == "plan":
            schedule = generate_schedule(subjects, deadlines, weakness, total_hours)

        elif action == "timetable":
            timetable = request.form.get('timetable')

        elif action == "productivity":
            used = float(request.form.get('used_hours', 0))
            wasted = float(request.form.get('wasted_hours', 0))

    return render_template_string(HTML, schedule=schedule, timetable=timetable, used=used, wasted=wasted)

# ================= AUTO OPEN =================
def open_browser():
    webbrowser.open("http://127.0.0.1:5000/")

if __name__ == "__main__":
    threading.Timer(1, open_browser).start()
    app.run(debug=True)