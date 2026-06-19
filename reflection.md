# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The first time I ran the game, it looked normal.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  A bug that I ran into was that I guessed a number way lower than the secret number but the hint told me to go lower. And vice versa for a number higher than the secret number.

  Another bug I noticed was that after guessing the secret number correctly and trying to start a new game, the new game button just did not work. It did not let me guess new numbers.

  Easy mode has less guess attempts than normal mode.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|guess of 4|go higher|go lower|none|
|Start a new game then guess a number|go higher/go lower|none|You already won. Start a new game to play again.|
|guess of 50|go lower|go higher|none|

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude Code 

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

The logic functions were in the app.py file so it suggested to move it and it was correct. AI suggestion - I'll move all four game logic functions to logic_utils.py, simplify where possible (combining redundant null checks, using max() instead of manual clamp, etc.), then update app.py to import from there. I verified with this final message from claude - app.py — removed the 40 lines of local function definitions, replaced with a single import line. All behavior is identical.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). 

One suggestion that was incorrect was needing to refactor logic for the high/low methods. Claude suggested to change the current code and add more lines but I thought the current logic was good so I denied it.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
When I tried it out myself on the refreshed streamlit page.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I did a pytest on the high/low guess logic and it showed that there were no errors in that logic after everything was refactored.
- Did AI help you design or understand any tests? How?
Yes, I gave it the description and it designed 10 tests for the high/low logic.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Reruns are like resetting the code and the session state are like the current memory

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Writing more comments and thinking about refactoring/changes to make code simpler and cleaner
- What is one thing you would do differently next time you work with AI on a coding task?
Try to use less but better, more concise prompts.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
It requires a lot more manual inspection than I thought if you want it to run exactly how you want to.