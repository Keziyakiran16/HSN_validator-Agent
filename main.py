# main.py
from Agent_workflow.agent import validate_hsn_tool

if __name__ == "__main__":
    while True:
        user_input = input("Enter an HSN code to validate (or 'exit'): ")
        if user_input.lower() == "exit":
            break
        prompt = f"Validate HSNCode {user_input}"
        result = validate_hsn_tool(prompt)
        print(result)
