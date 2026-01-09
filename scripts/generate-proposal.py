#!/usr/bin/env python3
"""
Quadspace Proposal Generator
Generates professional PDF proposals from JSON data files
"""

import json
import sys
import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML, CSS

def load_json_data(json_path):
    """Load proposal data from JSON file"""
    with open(json_path, 'r') as f:
        return json.load(f)

def generate_html(data, template_dir):
    """Generate HTML from template and data"""
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template('base-template.html')
    return template.render(**data)

def generate_pdf(html_content, css_path, output_path):
    """Generate PDF from HTML content"""
    css = CSS(filename=css_path)
    HTML(string=html_content, base_url=str(Path(css_path).parent)).write_pdf(
        output_path,
        stylesheets=[css]
    )

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate-proposal.py <data.json> [output.pdf]")
        sys.exit(1)
    
    # Get paths
    json_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else 'proposal.pdf'
    
    # Get script directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    template_dir = project_root / 'templates'
    css_path = template_dir / 'styles.css'
    
    # Load data
    print(f"Loading data from {json_path}...")
    data = load_json_data(json_path)
    
    # Generate HTML
    print("Generating HTML...")
    html_content = generate_html(data, str(template_dir))
    
    # Generate PDF
    print(f"Generating PDF to {output_path}...")
    generate_pdf(html_content, str(css_path), output_path)
    
    print(f"✓ Proposal generated successfully: {output_path}")

if __name__ == '__main__':
    main()
