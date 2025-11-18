# AI Product Manager Agent (CLI)

A command-line AI tool that acts as an expert Product Manager assistant. It interviews you about your product idea, generates a detailed Product Requirements Document (PRD), and outputs **Jira-compliant User Stories** (CSV format).

## Features

- **Interactive Discovery:** The AI asks you one question at a time to flesh out your idea.
- **Full PRD Generation:** Automatically compiles technical, functional, and non-functional requirements.
- **Jira-Ready Export:** Generates user stories formatted specifically for Jira import (Summary, Description, Labels).

## Prerequisites

You need to have **Python** installed on your computer.

- **Windows:** [Download Python here](https://www.python.org/downloads/) (Make sure to check the box "Add Python to PATH" during installation).
- **Mac/Linux:** You likely already have it. Open terminal and type `python3 --version` to check.

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
git clone https://github.com/kavishsekhri/PRD-User-Story-Creator.git
cd PRD-User-Story-Creator
```

**Step B: Create a Virtual Environment (Optional but Recommended)**

*Windows:*

```bash
python -m venv venv
venv\Scripts\activate
```

*Mac/Linux:*

```bash
python3 -m venv venv
source venv/bin/activate
```

**Step C: Install Requirements**

```bash
pip install -r requirements.txt
```

## How to Run

1. **Start the application:**

   ```bash
   python cli_app.py
   ```

   (Note: On Mac/Linux, if the above doesn't work, try typing `python3 cli_app.py`)

2. **Enter your API Key:** The app will ask for your Gemini API Key. Paste the key you got in Step 1 and press Enter.

3. **Chat with the Agent:** Answer the AI's questions about your product. It will guide you through the process.

4. **Get your CSV:** When the process is finished, the AI will print a CSV block.
   - Copy the CSV text from your terminal.
   - Save it as a file named `stories.csv`.
   - Import this file directly into Jira.

## Jira Import Mapping

When importing the `stories.csv` file into Jira, map the columns as follows:

| CSV Column | Map to Jira Field | Description |
|---|---|---|
| Summary | Summary | The concise goal of the story. |
| Description | Description | The full user story text ("As a... I want..."). |
| Labels | Labels | The User Role (e.g., Admin, User). |
