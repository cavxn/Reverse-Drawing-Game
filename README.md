Reverse Drawing Game

Welcome to **Reverse Drawing Game**, a fun and interactive AI-powered guessing game where the AI slowly sketches an object, and you have to guess what it is before the drawing is complete!

---

 🎯 Project Overview

Reverse Drawing Game is designed to challenge users to guess the object being drawn by the AI in real-time. The AI progressively sketches the object stroke by stroke, and the user has limited time to guess correctly. It’s a unique blend of art, AI, and gaming that’s both entertaining and mentally engaging.

---

 ⚙️ Features

- **Progressive Drawing**: The AI draws an object gradually, giving users multiple chances to guess.
- **Timed Guessing**: Users have a limited time (e.g., 5 seconds) to guess the drawing.
- **Multiple Difficulty Levels**: Adjust difficulty to make guessing easier or harder.
- **Hint System**: Get hints to help guess the drawing.
- **Round Limit & Scoring**: Play through several rounds and keep track of your score.
- **Drawing History**: Review previous drawings and guesses.
- **Dark Mode Support**: Switch between light and dark themes for a comfortable gaming experience.
- **Smooth User Interface**: Clean and responsive UI for an enjoyable experience.

---

 📋 How to Play

1. The AI starts drawing a random object from the dataset.
2. Watch as the drawing progresses stroke by stroke.
3. Type your guess into the input box.
4. Submit your guess before time runs out.
5. Points are awarded for correct and quick guesses.
6. Use hints if you’re stuck (limited number available).
7. Proceed to the next round until the game ends.

---

 🛠️ Technologies Used

- Python (backend logic)
- [QuickDraw Dataset](https://github.com/googlecreativelab/quickdraw-dataset) for AI drawing data
- Streamlit for web-based interactive UI
- Machine Learning/AI models for generating and rendering the drawings

---

 🚀 Installation & Setup

1. Clone the repository:
   bash
   git clone https://github.com/cavxn/Reverse-Drawing-Game.git
   cd Reverse-Drawing-Game

2. (Optional) Create a virtual environment:
  python3 -m venv venv
  source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. Install dependencies:
   pip install -r requirements.txt

4. Run the app
   streamlit run app.py


📁 Project Structure
Reverse-Drawing-Game/
│
├── app.py                  # Main Streamlit app file
├── drawing_generator.py    # AI drawing logic
├── game_logic.py           # Game mechanics and scoring
├── utils.py                # Utility functions
├── assets/                 # Static assets (images, icons)
├── requirements.txt        # Python dependencies
└── README.md               # This file


🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to fork the repo and submit a pull request.

Please ensure your code follows the existing style and includes appropriate tests where applicable.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgements
Google Creative Lab for the QuickDraw Dataset

Streamlit for making interactive web apps simple and fast

Open source community for continuous inspiration and support

📬 Contact
Created by Cavin S – feel free to reach out if you have any questions or suggestions!


If you want me to customize or add any specific sections (like screenshots, demo link, or technical details), just let me know!

