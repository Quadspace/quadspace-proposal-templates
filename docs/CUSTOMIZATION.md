_**Customization Guide**_

This guide explains how to customize the proposal templates, including styles, layout, and branding.

## Modifying Styles (CSS)

All visual styles are controlled by the `templates/styles.css` file. You can edit this file to change colors, fonts, spacing, and more.

### Key Style Classes

-   `.header`: Controls the top section with the logo and main title.
-   `.people-header`: The cyan-colored bar for the "People" section.
-   `.cost-table`: The table used for the investment summary.
-   `.signature-section`: The area for signatures at the end of the proposal.

### Changing Colors

To change the primary brand color, find and replace the hex code `#00BCD4` in `styles.css` with your desired color.

### Changing Fonts

The template uses the "Montserrat" font from Google Fonts. To change it, update the `@import` rule at the top of `styles.css` and modify the `font-family` property for the `body` tag.

## Modifying the Layout (HTML)

The main layout is defined in the `templates/base-template.html` file. This file uses the Jinja2 templating engine to insert data from your JSON files.

### Template Variables

Data from your JSON file is accessible using double curly braces, like `{{ client.name }}`.

### Adding or Removing Sections

You can add new sections by creating new `div` elements with appropriate classes. To remove a section, simply delete the corresponding HTML block.

### Loops and Conditionals

The template uses Jinja2 control structures to handle dynamic content:

-   **Loops**: `{% for phase in project.phases %}` iterates through the project phases.
-   **Conditionals**: `{% if client.logo %}` checks if a client logo is provided before trying to display it.

## Adding a New Logo

1.  Place your new logo image in the `assets/` directory.
2.  Update the `<img>` tag in `templates/base-template.html` to point to your new logo file:

```html
<img src="../assets/your-new-logo.png" alt="Quadspace Logo" class="logo">
```

## Print and PDF Optimization

The `styles.css` file includes a `@media print` block and `@page` rules to ensure the generated PDF looks clean and professional.

-   `page-break-inside: avoid;`: Prevents sections from being split across pages.
-   `page-break-after: avoid;`: Prevents page breaks directly after headings.
-   `@page`: Sets the page size (e.g., `letter`) and margins for the PDF output.

By following these guidelines, you can easily adapt the proposal template system to meet your specific branding and content needs.
