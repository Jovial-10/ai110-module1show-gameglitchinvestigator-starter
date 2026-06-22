# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
- [ ] Detail which bugs you found.
- [ ] Explain what fixes you applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. Open the app and select **Normal** difficulty from the sidebar (range 1–100, 8 attempts allowed). The secret number is generated once and stays fixed for the entire game
2. Enter a guess of **40** and click Submit. The game correctly returns 📈 **"Go HIGHER!"** and the attempt counter decreases by 1.
3. Enter a guess of **70**. The game correctly returns 📉 **"Go LOWER!"** — confirming the Higher/Lower hints are no longer swapped.
4. After each guess the score updates: wrong guesses deduct 5 points, and a win awards points based on how few attempts were used (earlier wins score higher, minimum 10 points).
5. Enter the correct number (e.g. **55**). The game displays 🎉 **"Correct!"**, launches balloons, shows the final score, and locks the input — a new game is required to play again.

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```
============================================================= test session starts ==============================================================
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0
rootdir: /Users/jovialrana/Documents/CodePath/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.7.0
collected 10 items                                                                                                                             

tests/test_game_logic.py ..........                                                                                                      [100%]

============================================================== 10 passed in 0.02s ==============================================================


## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
