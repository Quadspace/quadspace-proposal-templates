_**industrial-engineer.ai Proposal Generator**_

A professional, data-driven proposal generation system designed for industrial-engineer.ai. This system enables the creation of branded, print-ready, and Adobe-signable PDF proposals in under 60 seconds.

## Key Features

- **Ultra-Fast Generation**: Create professional proposals in under a minute from simple JSON data files.
- **industrial-engineer.ai Branding**: Dark theme with lime green accents matching your website aesthetic.
- **2-Page Maximum**: Optimized layout ensures proposals fit on exactly 2 pages for quick review.
- **Print-Ready & Signable**: Output is optimized for high-quality printing with signature blocks compatible with Adobe Acrobat.
- **Manus Integration Ready**: Structured question template enables voice-to-proposal workflows.

## Quick Start

### 1. Prerequisites

- Python 3.8+
- `pip` for package installation

### 2. Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/Quadspace/quadspace-proposal-templates.git
cd quadspace-proposal-templates
sudo pip3 install -r scripts/requirements.txt
```

### 3. Generate a Proposal

Create a new JSON data file in the `examples/` directory (or copy an existing one) and run the generation script:

```bash
python3 scripts/generate-proposal.py examples/your-new-proposal.json examples/your-new-proposal.pdf
```

Your new PDF proposal will be saved in the `examples/` directory.

## Manus Integration

This system is designed to work seamlessly with Manus for voice-to-proposal workflows. The structured question template in `docs/manus-question-template.md` guides Manus to ask the right questions and auto-fill proposal data.

### How It Works

1. **You speak to Manus**: "Create a proposal for Client X for a $5000 project with three phases..."
2. **Manus asks structured questions**: Following the template in `docs/manus-question-template.md`
3. **JSON data is generated**: Manus creates the proposal data file automatically
4. **PDF is created**: The generation script produces a professional 2-page proposal
5. **Ready to send**: Review and deliver to your client

## Documentation

- **[Usage Guide](./docs/USAGE.md)**: Detailed instructions on how to use the proposal generator.
- **[Customization Guide](./docs/CUSTOMIZATION.md)**: Learn how to modify templates and styles.
- **[Manus Question Template](./docs/manus-question-template.md)**: Structured questions for Manus integration.

## Repository Structure

```
quadspace-proposal-templates/
├── templates/           # HTML and CSS templates
├── assets/             # Logo and branding assets
├── examples/           # Example proposals and data files
├── scripts/            # Python generation scripts
└── docs/              # Documentation
```
