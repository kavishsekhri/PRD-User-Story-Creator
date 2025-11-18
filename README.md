# AI Product Manager Agent (CLI)

A command-line AI tool that acts as an expert Product Manager. It interviews you about your product idea, generates a detailed Product Requirements Document (PRD), and outputs **Jira-compliant User Stories** (CSV format).

## Features

*   **Interactive Discovery:** The AI asks you one question at a time to flesh out your idea.
*   **Full PRD Generation:** automatically compiles technical, functional, and non-functional requirements.
*   **Jira-Ready Export:** Generates user stories formatted specifically for Jira import (Summary, Description, Labels).

## Prerequisites

You need to have **Python** installed on your computer.
*   **Windows:** [Download Python here](https://www.python.org/downloads/) (Make sure to check the box "Add Python to PATH" during installation).
*   **Mac/Linux:** You likely already have it. Open terminal and type `python3 --version` to check.

## Setup Instructions

### 1. Get a Free Gemini API Key
This tool uses Google's Gemini AI model. You need a free key to use it.
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey).
2. Click **"Create API Key"**.
3. Copy the key string (it looks like `AlzaSy...`). You will need this in a moment.

### 2. Download and Install
Open your Terminal (Mac/Linux) or Command Prompt/PowerShell (Windows) and run these commands one by one:

**Step A: Download the code**
```bash
git clone <YOUR_GITHUB_REPO_LINK_HERE>
cd gemini_agent_webapp
