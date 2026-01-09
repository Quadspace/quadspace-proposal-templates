_**Usage Guide**_

This guide provides detailed instructions on how to use the Quadspace Proposal Generator to create professional, branded proposals.

## Creating a New Proposal

The entire process is driven by a single JSON data file. To create a new proposal, follow these steps:

### 1. Create a JSON Data File

Create a new file with a `.json` extension in the `examples/` directory. You can copy an existing file like `autocad-reverse-engineering.json` to get started.

### 2. Edit the JSON Data

Open your new JSON file and fill in the details for your proposal. The structure is explained below:

#### `client` Object

Contains information about the client.

-   `name`: The client's company name.
-   `location`: The client's city and state.
-   `logo`: (Optional) A relative path to the client's logo file. Store logos in `assets/client-logos/`.
-   `contacts`: A list of contact people at the client's company.

#### `quadspace` Object

Contains information about the Quadspace team members involved.

-   `contacts`: A list of Quadspace contacts.

#### `project` Object

Contains all the details about the project.

-   `title`: The main title of the proposal.
-   `overview`: A paragraph describing the project's objective.
-   `total_amount`: The total project cost (numeric).
-   `phases`: A list of project phases. Each phase is an object with:
    -   `name`: The name of the phase (e.g., "Define", "Execute").
    -   `description`: A paragraph explaining what the phase entails.
    -   `deliverables`: A list of specific deliverables for that phase.
    -   `amount`: The cost for that specific phase (numeric).

#### `terms` Object

Contains payment and scheduling terms.

-   `payment_schedule`: The payment terms (e.g., "Net 30").
-   `start_date`: The projected start date of the project.

### 3. Run the Generator Script

Open your terminal, navigate to the `quadspace-proposal-templates` directory, and run the following command:

```bash
python3 scripts/generate-proposal.py examples/your-proposal-file.json examples/your-proposal-output.pdf
```

-   Replace `your-proposal-file.json` with the name of your data file.
-   Replace `your-proposal-output.pdf` with the desired name for your output PDF.

Your new proposal will be generated and saved in the `examples/` directory.

## Voice-to-Proposal Workflow (Future)

This system is designed for future integration with Manus to enable a seamless voice-to-proposal workflow:

1.  **Speak to Manus**: "Create a proposal for Client X for a $5000 project with three phases..."
2.  **Data Extraction**: Manus will parse the voice input and structure it into the required JSON format.
3.  **File Generation**: Manus will automatically create the JSON data file.
4.  **PDF Creation**: The `generate-proposal.py` script will be triggered to create the final PDF.
5.  **Delivery**: The generated proposal will be presented for review and delivery.

This automated workflow will reduce the time to create a professional proposal to just a few minutes.
