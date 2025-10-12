# EduTrack — Learning Progress Tracker

cat > README.md << EOF
# EduTrack — Learning Progress Tracker

EduTrack is a web application designed to help learners track their study goals, progress, and study sessions through an interactive dashboard.
EduTrack aims to provide an accessible and easy-to-use platform for learners to manage and visualize their learning journey.

---

## Features

- User authentication (signup, login, logout)  
- Create, update, and delete learning goals  
- Visual progress tracking with charts (using Chart.js)  
- Pomodoro-style study timer to manage sessions  
- Export progress reports as CSV files  
- *(Stretch goal)* AI-generated study tips using OpenAI API  

---

## Tech Stack

- Backend: Flask (Python)  
- Database: PostgreSQL (or SQLite for local development)  
- Frontend: HTML, CSS, JavaScript  
- Charting: Chart.js  
- Deployment: Render or Heroku  

---

## Setup & Installation

1. **Clone the repository**

   \`\`\`bash
   git clone https://github.com/yourusername/edutrack.git
   cd edutrack
   \`\`\`

2. **Create and activate a virtual environment**

   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   \`\`\`

3. **Install dependencies**

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Set up the database**

   - For local testing, SQLite is preconfigured. For production, update \`config.py\` with your PostgreSQL URI.

5. **Run the Flask app**

   \`\`\`bash
   flask run
   \`\`\`

6. **Open your browser**

   Navigate to \`http://127.0.0.1:5000\` to use EduTrack locally.

---

## Usage

- Register a new account or login.  
- Create learning goals and track progress.  
- Use the built-in timer to manage study sessions.  
- Export your progress reports for offline review.

---

## Future Improvements

- Integration with OpenAI API for personalized study tips  
- User profile customization  
- Email notifications and reminders  
- Gamification with badges and streak tracking  

---

## About Me

Hi! I'm Brenda Iradukunda, a Computer Science and Economics major from Washington and Lee University, passionate about building impactful software and creating innovative solutions.
---

## License

This project is licensed under the MIT License.  

---

Feel free to reach out or contribute!

EOF



