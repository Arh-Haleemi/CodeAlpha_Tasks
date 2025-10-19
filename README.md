# CodeAlpha_Python_Tasks
This repository contains all CodeAlpha internship Python tasks in one organized project.   Each folder represents an independent project demonstrating practical Python skills — from beginner to intermediate.

🧭 Main Launcher (Code Alpha Internship - Project Launcher)

main.py serves as the central launcher to run or test any of the project modules from a single place. Useful for quickly switching between tasks during development and demos.

📌 Features

Menu-driven interface to select and run individual modules.

Validates user input and routes to the corresponding script function.

Option to run all tasks sequentially or exit cleanly.

🛠 Concepts Used

Function imports and modular code organization

input() for simple CLI menus

Error handling and flow control (try/except, loops)

if __name__ == "__main__" pattern for script entry

🎮 Hangman Game (Code Alpha Internship - Task 1)

This is a simple text-based Hangman Game in Python, created as part of Task 1 of the Code Alpha Internship.
The player guesses words one letter at a time, with a maximum of 6 incorrect guesses allowed.

📌 Features

Predefined list of 5 words (no external file or API needed).

Player has 6 incorrect guesses before the game is over.

Console-based input/output (no graphics or audio).

Supports multiple words — you can try to complete all words in the list.

Displays progress, guessed letters, and completed words.

🛠 Concepts Used

random module for word selection

while loop for game continuation

if-else conditions for logic handling

Strings and Lists for storing and updating game progress

💼 Portfolio Tracker (Code Alpha Internship - Task 2)

A lightweight command-line Stock Portfolio Tracker that helps manage holdings, compute totals, and export portfolio snapshots to CSV.

📌 Features

Add, edit, and remove holdings (symbol, quantity, price).

Compute total investment value and per-asset contribution.

Export portfolio summary to a CSV file for offline analysis.

Simple, human-readable console output for quick checks.

🛠 Concepts Used

File I/O with csv module for persistence/export

Dictionaries and lists for structured data storage

Basic arithmetic and aggregation (sums, totals)

Input validation and simple persistence patterns

🛠 Task Automation Utilities (Code Alpha Internship - Task 3)

A collection of small automation utilities to speed up common tasks: moving image files, extracting email addresses from text, and scraping webpage titles.

📌 Features

Move .jpg/.png files from one folder to another (batch file mover).

Extract email addresses from text files using regex and save results.

Scrape and return the <title> of a web page using requests + BeautifulSoup.

CLI menu to choose and run any automation task.

🛠 Concepts Used

os and shutil for file system operations

re (regular expressions) for email extraction

requests and bs4 (BeautifulSoup) for simple web scraping

Error handling for network and file I/O

🤖 Rule-Based Chatbot (Code Alpha Internship - Task 4)

A minimal rule-based chatbot that replies to user inputs using predefined patterns and responses — great for learning pattern matching and dialog flow basics.

📌 Features

Pattern-matching responses (greetings, farewell, help, simple Q&A).

Keeps conversation in the terminal with a friendly prompt.

Easy to extend with more rules or a simple dictionary of replies.

Provides examples of how to parse and respond to user input.

🛠 Concepts Used

String processing and normalization (lower(), strip())

Conditional logic and pattern detection (keywords, startswith/contains)

Loops to maintain conversation until exit command

Simple mapping/dictionary-based response lookup
