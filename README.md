_**Quadspace Proposal Generator**_

This repository contains a professional, data-driven proposal generation system designed for Quadspace. It enables the creation of branded, print-ready, and Adobe-signable PDF proposals in minutes.

## Quick Start

### 1. Prerequisites

- Python 3.8+
- `pip` for package installation

### 2. Installation

Clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd quadspace-proposal-templates
sudo pip3 install -r scripts/requirements.txt
```

### 3. Generate a Proposal

Create a new JSON data file in the `examples/` directory (or copy an existing one) and run the generation script:

```bash
python3 scripts/generate-proposal.py examples/your-new-proposal.json examples/your-new-proposal.pdf
```

Your new PDF proposal will be saved in the `examples/` directory.

## Features

- **Data-Driven**: Proposals are generated from simple JSON files, making automation easy.
- **Branded**: Templates are designed with Quadspace branding for a consistent, professional look.
- **Print-Ready**: CSS is optimized for high-quality printing and PDF conversion.
- **Adobe Signable**: Includes designated signature blocks compatible with Adobe Acrobat.
- **Modular**: Easily define project phases, deliverables, and costs.

## Documentation

- **[Usage Guide](./docs/USAGE.md)**: Detailed instructions on how to use the proposal generator.
- **[Customization Guide](./docs/CUSTOMIZATION.md)**: Learn how to modify templates and styles.

## Future Integration

This system is designed to be integrated with Manus for voice-to-proposal workflows, enabling ultra-fast quote generation directly from voice commands.
