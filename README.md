#  Smart Study Planner (AI/ML Project)

An AI-powered web application that helps students manage their time effectively by generating adaptive study schedules, personalized timetables, and productivity analytics.



##  Features

###  AI Study Plan Generator

* Generates a smart study schedule based on:

  * Subject deadlines
  * Weakness level (1–5)
  * Total available study hours
* Uses a priority-based recommendation system



###  Personalized Timetable

* Users can input their daily routine
* Displays timetable separately on the interface


###  Productivity Tracker

* Visualizes performance using a pie chart
* Shows:

  * Used hours
  * Wasted hours



###  Modular Controls

* Separate buttons for:

  * Generate Study Plan
  * Show Timetable
  * Show Productivity Chart



###  Modern UI

* Neon dark theme 🌌
* Clean and responsive design
* Dynamic subject input fields



##  AI/ML Concepts Used

###  Priority Prediction Model

Priority = (Weakness × 2) + (10 / (Days Left + 1))

* Higher weakness → More focus
* Closer deadline → Higher urgency



###  Adaptive Time Allocation

Allocated Hours = (Priority / Total Priority) × Total Study Hours

* Ensures intelligent distribution of study time



###  Recommendation System

* Subjects are ranked and scheduled based on calculated priority



## Tech Stack

* Backend: Python
* Framework: Flask
* Frontend: HTML, CSS, JavaScript
* Visualization: Chart.js
* Data Handling: Pandas

---

## 📂 Project Structure

app.py  → Complete single-file application

---

## ▶️ How to Run

1. Install dependencies:
   pip install flask pandas

2. Run the application:
   python app.py

3. Open in browser:
   http://127.0.0.1:5000/

---

## 🎯 How It Works

1. Enter:

   * Subjects
   * Deadlines
   * Weakness level
   * Total study hours

2. Choose an action:

   * Generate Study Plan
   * Show Timetable
   * Show Productivity

3. The system:

   * Calculates subject priority
   * Allocates study hours
   * Displays results visually



 📊 Output

* Day-wise study schedule
* Hours assigned per subject
* Custom timetable display
* Productivity pie chart



 ⚠️ Limitations

* Rule-based model (not trained ML model)
* No database or user login
* Productivity tracking is manual



🔮 Future Improvements

* Real Machine Learning model
* User authentication system
* Database integration
* Mobile-friendly UI
* Deployment on web


##  Academic Value

This project demonstrates:

* AI-based decision making
* Recommendation systems
* Time optimization techniques
* Full-stack development using Python



## 👨‍💻 Author

ISHANT MAKKAR



## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
