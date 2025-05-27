# agent.py
import os
import pandas as pd
import re
from dotenv import load_dotenv
from google.adk.agents import Agent

load_dotenv()
DATA_URL = os.getenv("DATA_URL")

# Load and clean dataset
hsn_df = pd.read_csv(DATA_URL)
hsn_df.columns = hsn_df.columns.str.strip()
print("Loaded columns:", hsn_df.columns.tolist())

# Define HSN validation tool
def validate_hsn_tool(prompt: str) -> str:
    match = re.search(r"\b\d{1,}\b", prompt)
    if not match:
        return " Please provide a valid HSN code ."

    hsn_code = match.group()
    
    if 'HSNCode' not in hsn_df.columns:
        return " 'HSNCode' column not found in dataset."

    result = hsn_df[hsn_df['HSNCode'].astype(str) == hsn_code]

    if not result.empty:
        return f" Valid HSN Code: {result.iloc[0]['Description']}"
    else:
        return " Invalid HSN Code."

# Define root agent
root_agent = Agent(
    name="ValidateHSNCode",
    model="gemini-2.0-flash-exp",
    description="Validates HSN codes using a master dataset.",
    instruction="Use the tool to validate the HSN code.",
    tools=[validate_hsn_tool],
)
