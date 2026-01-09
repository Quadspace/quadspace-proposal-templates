_**Manus Proposal Generation - Question Template**_

This document outlines the structured questions Manus should ask to gather the necessary information for generating a new proposal. The answers will be used to populate the `proposal-data.json` file.

## Instructions for Manus

1.  Ask the user the following questions sequentially.
2.  Use the user's answers to construct the JSON data object.
3.  Ensure all required fields are captured.
4.  Confirm the total project amount and phase amounts are correct.
5.  Trigger the `generate-proposal.py` script with the new JSON data.

--- 

### **Part 1: Client Information**

1.  **Client Company Name**: What is the full name of the client's company?
2.  **Client Location**: Where is the client located (City, State)?
3.  **Client Contacts**: Who are the main points of contact at the client's company? Please provide their full names and titles.

### **Part 2: Project Details**

1.  **Project Title**: What is the official title of this project?
2.  **Project Overview**: Can you provide a brief, one-paragraph overview of the project's objectives and goals?
3.  **Total Project Amount**: What is the total investment for this project?

### **Part 3: Project Phases (Repeat for each phase)**

*For each phase of the project (e.g., Define, Execute, Enhancements), please provide the following information:*

1.  **Phase Name**: What is the name of this phase?
2.  **Phase Description**: Please describe the activities and goals of this phase in a short paragraph.
3.  **Phase Deliverables**: What are the key deliverables for this phase? (List 3-5 items)
4.  **Phase Amount**: What is the cost for this specific phase?

### **Part 4: Your Information**

1.  **Your Contacts**: Who from your team should be listed on the proposal? Please provide their full names and titles.

### **Part 5: Terms & Conditions**

1.  **Payment Schedule**: What are the payment terms (e.g., Net 30, 50% upfront)?
2.  **Project Start Date**: What is the projected start date for this project?

--- 

## Example JSON Output Structure

```json
{
  "client": {
    "name": "...",
    "location": "...",
    "contacts": [
      {"name": "...", "title": "..."}
    ]
  },
  "quadspace": {
    "contacts": [
      {"name": "...", "title": "..."}
    ]
  },
  "project": {
    "title": "...",
    "overview": "...",
    "total_amount": 0,
    "phases": [
      {
        "name": "...",
        "description": "...",
        "deliverables": ["..."],
        "amount": 0
      }
    ]
  },
  "terms": {
    "payment_schedule": "...",
    "start_date": "..."
  }
}
```
