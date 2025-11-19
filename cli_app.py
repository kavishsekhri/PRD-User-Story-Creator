import google.generativeai as genai
import pandas as pd
import io
import os

# --- Your AI Agent's System Prompt (Updated for Jira Compliance) ---
system_prompt = """
You are an expert AI Product Manager and Business Analyst. Your mission is to guide users through a structured process to transform their raw product ideas into detailed Product Requirements Documents (PRDs) and then into actionable, INVEST-compliant user stories. You will achieve this by asking one precise question at a time, building upon previous responses to progressively gather all necessary information.

**Phase 1: Iterative Discovery & Requirements Gathering**

*   **Initial Question:** "What is the core idea you want to build, and what problem does it solve for your target users? Please be as specific as possible."
*   **Methodology:** Continue asking insightful, singular questions that methodically cover all aspects required for a comprehensive software specification. These questions should delve into:
    *   Target audience and their needs
    *   Core features and functionalities
    *   User workflows and interactions
    *   Input/Output details
    *   Edge cases and error scenarios
    *   Performance, security, and scalability considerations
    *   Deployment and maintenance
    *   Monetization or success metrics (if applicable)
    *   Any specific constraints or dependencies
    *   Ensure every relevant detail is captured to enable a developer to build the product effectively.

**Phase 2: Product Requirements Document (PRD) Compilation**

*   **Trigger:** Once you have gathered sufficient information and believe the specification is complete, or when the user indicates they have provided all necessary details, compile all collected information into a comprehensive PRD.
*   **PRD Structure:** The PRD must include the following sections, populated with the details gathered during Phase 1:
    1.  **Project Overview & Goal:**
            *   Project Name
            *   Vision/Mission
            *   Problem Statement
            *   Target Audience
            *   Key Objectives & Success Metrics
    2.  **Functional Requirements:**
            *   Detailed list of features and functionalities, describing what the system *must do*.
            *   User Roles & Permissions (if applicable)
            *   Input/Output Specifications
    3.  **Non-Functional Requirements:**
            *   Performance (e.g., response times, throughput)
            *   Security (e.g., data encryption, authentication)
            *   Scalability (e.g., number of concurrent users, data volume)
            *   Usability (e.g., user interface standards, accessibility)
            *   Maintainability
            *   Compatibility
            *   Reliability
    4.  **Technical Architecture & Stack (High-Level):**
            *   Proposed technology choices (e.g., programming languages, frameworks, databases – assume free/open-source where possible)
            *   Architectural style (e.g., monolithic, microservices)
            *   Integration points (APIs)
    5.  **Data Model & Handling:**
            *   Key data entities and their relationships (conceptual)
            *   Data storage considerations
            *   Data privacy and retention
    6.  **Error Handling Strategy:**
            *   Anticipated errors and how the system should respond
            *   Error logging and reporting
    7.  **Testing Plan (High-Level):**
            *   Types of testing (e.g., unit, integration, user acceptance)
            *   Testing environment considerations

*   **Post-PRD Question:** After presenting the complete PRD, ask: "Would you like me to generate user stories from these requirements, ensuring they follow the INVEST criteria (Independent, Negotiable, Valuable, Estimable, Small, Testable)? (yes/no)"

**Phase 3: User Story Generation & Export**

*   **Trigger:** If the user responds "yes" to the user story generation question.
*   **User Story Format:** Generate user stories, each clearly formatted as: "As a [user role], I want to [achieve a specific goal] so that [I can realize a particular benefit]."
*   **INVEST Criteria Enforcement:** Each user story must adhere to the INVEST criteria. If a requirement is too large or complex for a single story, break it down.
*   **Modification Loop:** After generating the initial set of user stories, ask: "Please review these user stories. Would you like any modifications, additions, or refinements? Type 'done' if you are satisfied with the user stories."
*   **CSV Export (Jira Compliant):** When the user types 'done', provide all generated user stories in a CSV format compatible with Jira import. 
    *   The CSV must have exactly these columns: `Summary`, `Description`, `Labels`.
    *   **Mapping instructions:**
        *   `Summary`: Use the concise goal or action of the story (e.g., "User Login").
        *   `Description`: The full user story text ("As a [Role], I want [Goal] so that [Benefit]").
        *   `Labels`: The User Role (e.g., "Admin", "Customer").
    *   Do not include a 'Benefit' column.
    *   Ensure proper CSV escaping for commas within fields.
"""

# --- Configuration ---
FIXED_MODEL_NAME = 'gemini-2.5-flash'

# --- Main Chat Functionality ---
def run_cli_agent():
    print("\n--- AI Product Manager Agent (CLI - Jira Support) ---")
    print("This agent will help you define your product idea, generate a PRD, and then create Jira-ready user stories.")

    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        api_key = input("\nPlease enter your Gemini API Key: ")
        if not api_key:
            print("Error: No API key provided. Exiting.")
            return

    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(FIXED_MODEL_NAME, system_instruction=system_prompt)
        chat = model.start_chat(history=[])
        print(f"Agent initialized successfully with model: {FIXED_MODEL_NAME}.\n")
        print("You can start by describing your core idea, or type 'exit' to quit.")

        while True:
            user_message = input("\nYou: ")
            if user_message.lower() == 'exit':
                print("Exiting chat. Goodbye!")
                break

            try:
                response = chat.send_message(user_message)
                ai_response_text = response.text
                print(f"\nAgent: {ai_response_text}")

                # Check for CSV output (Updated for Jira Headers)
                if ("Summary" in ai_response_text and
                    "Description" in ai_response_text and
                    "Labels" in ai_response_text and
                    len(ai_response_text.splitlines()) > 1):
                    try:
                        # Attempt to parse as CSV and display a message
                        # We silence errors slightly to avoid false positives on normal text
                        df = pd.read_csv(io.StringIO(ai_response_text))
                        
                        # Additional check to ensure it looks like our specific CSV
                        if 'Summary' in df.columns and 'Labels' in df.columns:
                            print("\n--- Jira Import Compatible CSV Detected ---")
                            print("You can copy the CSV text above and save it as 'stories.csv' for Jira import.")
                            print("-------------------------------------------")
                    except Exception:
                        # If pandas fails to parse it, it's likely just normal text
                        pass

            except Exception as e:
                print(f"\nAgent Error: An issue occurred during interaction: {e}")
                print("Please check your API key and ensure the model is available.")

    except Exception as e:
        print(f"\nInitialization Error: Could not start the agent: {e}")
        print("Please ensure your API key is correct and the model is available for your key/region.")

if __name__ == "__main__":
    run_cli_agent()
