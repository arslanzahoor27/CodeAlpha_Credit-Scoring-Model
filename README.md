# Rule-Based AI Chatbot

A deterministic, rule-based chatbot built in Python utilizing an Intent-based Architecture. This project serves as the foundational deterministic layer before integrating Generative AI (LLMs).

## Core Concepts Implemented
* **IPO Pipeline:** Continuous Input, Process, and Output loop.
* **Input Sanitization:** Normalizing user text (lowercasing, whitespace stripping, punctuation removal) for accurate matching.
* **Intent Architecture:** Using dictionaries (Hash Maps) to map multiple user inputs to a single intent, avoiding inefficient conditional ladders.
* **Graceful Fallback:** Handling unmatched queries without crashing the system.

## How to Run
1. Clone the repository.
2. Open terminal and run: `python rule_chatbot.py`
3. Type your query. Type 'exit' to quit the application.

## Tech Stack
* Python 3
* Git & GitHub for Version Control