# Religion Weaponized eBook

## Project Overview  
This repository hosts two independent digital publications and their tooling:

1. **Religion Weaponized** — a digital publication exploring sensitive themes related to religion and its impact on society, providing in-depth analysis, resources, and support for survivors of religious trauma.  
2. **Brain & Neuroscience Basics** — a standalone educational e-book and Python PDF generator covering the fundamentals of neuroscience for beginners (see section below).

---

## Brain & Neuroscience Basics — E-Book Generator

The repository also includes a complete, stand-alone e-book generator for the title  
**"Brain & Neuroscience Basics — A Practical Guide to Understanding Your Mind and Using It Better"**.

### Contents

| # | Chapter |
|---|---------|
| — | Introduction |
| 1 | What Is the Brain? |
| 2 | Structure of the Brain |
| 3 | Neurons and Neural Communication |
| 4 | Brain Chemistry — Neurotransmitters |
| 5 | Neuroplasticity: How the Brain Changes |
| 6 | Memory and Learning |
| 7 | Attention and Focus |
| 8 | Emotions and the Brain |
| 9 | Decision-Making and Behaviour |
| 10 | Habits and the Brain |
| 11 | Stress and the Nervous System |
| 12 | Sleep and Brain Function |
| 13 | Practical Applications |
| — | Conclusion |

### How to Generate the PDF

**Prerequisites**

```bash
pip install -r requirements.txt
```

**Generate**

```bash
python neuroscience_ebook_generator.py
```

This produces `brain_neuroscience_basics.pdf` in the current directory.  
The PDF includes a styled title page, table of contents, all 13 chapters with subheadings, callout boxes, tip boxes, and a daily protocol table.

---

## Quick Start Guide  
To use the Religion Weaponized eBook, follow these steps:
1. Download the eBook from the repository.
2. Open it using any eBook reader or compatible software.
3. Explore the contents based on your interests.

## File Structure  
- `cover/`: Contains the book cover images.
- `content/`: Main text and chapters of the eBook.
- `assets/`: Additional resources and graphics.
- `book_cover_generator.py`: Generates a PNG cover for the Religion Weaponized title.
- `neuroscience_ebook_generator.py`: Generates the Brain & Neuroscience Basics PDF e-book.

## Design Features  
- Responsive layout for diverse devices.
- Interactive elements for enhanced user engagement.
- Accessibility options for all readers.

## E-book Content Breakdown  
- Introduction to the themes of the book.
- Detailed chapters exploring various aspects of the content.
- Resources section with links to further reading and support services.

## Technology Stack  
- Frontend: HTML, CSS, JavaScript
- Backend: Node.js for content management
- PDF generation: Python + ReportLab
- Deployment: Google Cloud Services for hosting and scalability.

## Customization Options  
Users can customize content through:
- Modifying chapter text.
- Adding personal reflections or notes.
- Theming options for UI.

## Deployment Instructions for Google Cloud  
1. Set up a Google Cloud account if you don't have one.
2. Create a new project in the Google Cloud Console.
3. Deploy the eBook content using Google App Engine or Cloud Storage for static content.
4. Monitor usage and analytics through Google Cloud Monitoring.

## Resources for Survivors  
- Links to support organizations.
- Material for healing and coping strategies.
- Community forums for sharing experiences.  

---  
*For additional information, consult the project documentation or contact the project maintainers.*