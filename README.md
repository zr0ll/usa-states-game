# 🇺🇸 USA States Game 🗺️

This is a fun and educational Python project built as part of Angela Yu's "100 Days of Code" bootcamp.

The goal is to correctly guess all 50 U.S. states by typing their names, which are then displayed on an interactive map.

---

## 🎮 How to Play

- Run the program by executing `main.py`.
- A blank map of the United States will appear.
- Type the name of a U.S. state (e.g., `Texas`, `California`).
- If correct, the state's name will appear in the correct location on the map.
- The game continues until all 50 states are guessed or the user exits by typing `Exit`.

---

## 🛠️ Technologies Used

- **Python**
- **Turtle** – for graphics and interaction
- **Pandas** – for reading and working with the CSV file

---

## 📁 Files Included

- `main.py` – the main Python file with the game logic
- `50_states.csv` – contains the list of U.S. states and their X/Y coordinates
- `blank_states_img.gif` – the blank map of the United States
- `states_to_learn.csv` – generated automatically when the user exits the game.  
  This file lists all the states that were not guessed, so the player can practice them later.

---

## 💡 Features

- Real-time map interaction using the Turtle graphics library
- CSV-based data handling with Pandas
- Creates a personalized learning file (`states_to_learn.csv`) for future practice

---

## ✅ Future Improvements

- Add score tracking
- Add a timer or leaderboard
- Support case-insensitive input or handle typos
- Add sound effects or background music

---

## 🧠 What I Learned

- How to use Turtle for GUI-based Python projects
- How to read and manipulate CSV files with Pandas
- How to build interactive games and track user input
- How to export user-specific data to a file (`states_to_learn.csv`)

---

## 👤 Author

Created by **Ron Ostapov** as part of the Python Bootcamp by Angela Yu.
