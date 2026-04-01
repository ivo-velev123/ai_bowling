# Bowling Kata: GEMINI.md

## Project Overview
Create a program that calculates the total score for a valid sequence of American Ten-Pin Bowling rolls.

## Core Mandates
- **Task Scope:** You are strictly tasked with writing the **tests only**. 
- **Wait for Implementation:** You must write **exactly one test at a time** and wait for the user to provide the implementation before writing the next test.
- **Do Not Implement:** Do not write any code to pass the tests yourself.
- **Development Process:** Follow strict **Test Driven Development (TDD)**.
- **Language:** Python.
- **Architecture & Style:**
  - Prioritize **encapsulation**.
  - Adhere to **Clean Code** principles.
  - Maintain high idiomatic quality.

## Domain Rules (Scoring Summary)
- A game consists of 10 frames.
- **Open Frame:** Score is the sum of two rolls (< 10 pins).
- **Spare (`/`):** 10 pins in two rolls. Score = 10 + next roll.
- **Strike (`X`):** 10 pins in one roll. Score = 10 + next two rolls.
- **10th Frame:** 
  - Spare grants 1 bonus roll.
  - Strike grants 2 bonus rolls.
  - Bonus rolls only count toward the 10th frame score.
- **Input:** A string representation (e.g., `"X 45 4/ 32"`).
- **Output:** Integer total score.

## Out of Scope
- Validation of rolls/input format.
- Checking for the correct number of rolls/frames.
- Intermediate frame scores.

## Workflow Execution
1. Identify the next simplest test case.
2. Write **exactly one** test using **pytest**.
3. Ensure the test fails (Red phase).
4. Wait for the user to implement the code to pass the test (Green phase).
5. Repeat.
