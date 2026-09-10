---
name: notes-ocr
description: >
  Digitizes handwritten scanned notes, PDFs, or images into structured professional documents.
  Use this skill whenever a user uploads a photo, scan, PDF, or image containing handwritten
  content — notes, diagrams, architecture sketches, plans, tables, flowcharts, lists — and
  wants it transcribed, organized, or converted into clean digital output. Triggers include:
  "digitize my notes", "convert this scan", "transcribe my handwriting", "turn this into a doc",
  "OCR this", "clean up my notes", "my handwritten PDF", "my photo of notes", or when the user
  uploads any image/PDF and asks for markdown, Excel, or PDF output. Always produce ALL THREE
  outputs (Markdown with Mermaid diagrams, Excel, and PDF) unless the user explicitly asks for
  fewer. The Mermaid diagrams must faithfully reconstruct any hand-drawn diagrams, entity maps,
  flowcharts, or relationship sketches exactly as drawn — not as a generic interpretation.
---

# Notes OCR Skill

Converts handwritten scanned notes, PDFs, or images into three clean professional outputs:
**Markdown** (with faithful Mermaid diagrams), **Excel** (structured data), and **PDF** (print-ready).

---

## Overview

When a user uploads handwritten content, follow these phases in order:

1. **Read & Extract** — parse every piece of content from the image/PDF
2. **Reconstruct Diagrams** — convert hand-drawn diagrams to Mermaid syntax exactly as drawn
3. **Structure Content** — organize all text into logical sections
4. **Generate Outputs** — produce MD + XLSX + PDF in parallel

---

## Phase 1: Read & Extract

### Supported Input Types
- Scanned PDFs (single or multi-page)
- Photos of handwritten notes
- Images (PNG, JPG, WEBP)
- Mixed content (text + diagrams on same page)

### What to Extract (miss nothing)
- All text, titles, headings, bullet points, numbered lists
- Every table (rows, columns, headers, sample data)
- Every diagram: flowcharts, entity maps, ERDs, org charts, mind maps, architecture sketches, arrow relationships
- Field labels and their types (e.g. "str: username", "Bool: KYC")
- Annotations, formulas, legends, footnotes
- Dates, authors, version numbers in headers/footers

### Extraction Pass
Read the input carefully top-to-bottom, left-to-right. For multi-page inputs, process each page fully before moving on. Keep a running structured outline:

```
## Page N
### Section (heading or inferred)
- bullet / text content
- [DIAGRAM] description of what was drawn
- [TABLE] header1 | header2 | ...
```

---

## Phase 2: Reconstruct Diagrams as Mermaid

This is the most critical phase. Every hand-drawn diagram must become a Mermaid block.

### Diagram Type Detection

| What you see in notes | Mermaid type to use |
|---|---|
| Boxes with arrows between them | `graph TD` or `graph LR` |
| Entity boxes with field lists | `graph TD` with subgraphs, or `erDiagram` |
| Hierarchy / tree structure | `graph TD` |
| Sequential steps / flow | `flowchart TD` |
| Database tables with relationships | `erDiagram` |
| Timeline or process phases | `graph LR` |
| Referral / network chains | `graph LR` or `graph TD` |
| CRUD labels on arrows | `graph TD` with edge labels |
| Nested groups / subgraphs | `graph TD` with `subgraph` blocks |

### Faithfulness Rules

- **Preserve the exact topology** — if A→B→C in the notes, write exactly that
- **Preserve labels verbatim** — field names, type annotations (str/bool/float/int), entity names, arrow labels must match the handwriting exactly (correct obvious misspellings but keep meaning)
- **Preserve hierarchy** — parent→child relationships, nesting, grouping as drawn
- **Do not add nodes or arrows not in the notes**
- **Do not simplify** — if there are 4 wallet types drawn, show all 4

### Mermaid Syntax Reminders
- Node labels with special chars: `A["str: wallet_id"]`
- Subgraphs: `subgraph Name \n ... \n end`
- Edge labels: `A -->|has a| B`
- ER entities: `ENTITY { type field_name }`
- Dotted arrows: `A -.->|optional| B`

### One Mermaid block per diagram
Each distinct diagram in the notes gets its own fenced ` ```mermaid ` block placed inline where that diagram appeared in the notes.

---

## Phase 3: Structure Content

Organize extracted content into document sections. Infer logical groupings from context:

- Use headings from the notes as section headers
- Group related bullet points under the nearest heading
- Place tables close to their surrounding text
- Insert Mermaid blocks exactly where the diagram appeared (not at the end)
- Add a Table of Contents at the top

### Markdown Template

```markdown
# [Document Title]

**Author:** [if visible] | **Date:** [if visible]

---

## Table of Contents
1. [Section 1]
2. [Section 2]
...

---

## [Section 1]
[content, tables, mermaid blocks inline]

## [Section 2]
...
```

---

## Phase 4: Generate All Three Outputs

Run all three output scripts. See `scripts/` for reusable helpers.

### Output 1 — Markdown (`[title].md`)

- Full document with all sections
- Mermaid diagram blocks inline, faithfully reconstructed
- Tables as GFM markdown tables
- Saved to `/mnt/user-data/outputs/`

### Output 2 — Excel (`[title].xlsx`)

Use `openpyxl`. Follow `scripts/build_excel.py` pattern:

- **One sheet per major section** of the document
- Sheet 1 always: "Overview" — title, date, author, section list
- Subsequent sheets: structured tables from each section
- If a section has no tabular data, create a two-column sheet: Field | Value, listing all key info
- Diagrams sheet: text description of each diagram and which Mermaid block it corresponds to
- Professional formatting: Arial font, `#366092` header fill, white header text, thin borders, alternating row fill `#F0F0F0`
- Run `scripts/recalc.py` after saving (copied from xlsx skill)

### Output 3 — PDF (`[title].pdf`)

Use `reportlab`. Follow `scripts/build_pdf.py` pattern:

- Title page: document name, author, date, short abstract
- Table of contents page
- One section per page-break where content is long
- Tables via `reportlab.platypus.Table` with `TableStyle`
- For each diagram: a clearly titled box stating "Diagram: [name] — see Mermaid block in Markdown file" plus a text-art approximation if the diagram is simple enough, otherwise a clean prose description
- Header color: `#366092`, white text; body: Arial 10pt; headings: Arial Bold 12-14pt
- Footer with page numbers and document title

### Naming Convention
Derive `[title]` from the document's heading or content (snake_case, no spaces).

---

## Calling the Scripts

```python
# After extracting content, build outputs:
import subprocess

# 1. Generate Excel
subprocess.run(['python', '/home/claude/notes-ocr/scripts/build_excel.py',
                '--data', data_json_path, '--out', output_xlsx_path])

# 2. Generate PDF
subprocess.run(['python', '/home/claude/notes-ocr/scripts/build_pdf.py',
                '--data', data_json_path, '--out', output_pdf_path])
```

Or write the scripts inline for the specific document — the script files are reference templates.

---

## Output Checklist

Before presenting files, verify:

- [ ] Markdown has a ToC
- [ ] Every hand-drawn diagram has a Mermaid block
- [ ] Mermaid topology matches the notes exactly (same nodes, same arrows)
- [ ] All tables from the notes are present in Markdown
- [ ] Excel has one sheet per section, professional formatting
- [ ] PDF has title page, ToC, all sections, proper headers/footers
- [ ] All three files are in `/mnt/user-data/outputs/`
- [ ] `present_files` called with all three paths

---

## Reference Scripts

See `scripts/` directory:

- `build_excel.py` — reusable Excel builder (openpyxl, professional style)
- `build_pdf.py` — reusable PDF builder (reportlab, professional style)
- `excel_styles.py` — shared style constants for Excel
- `pdf_styles.py` — shared style constants for PDF

These are **templates** — copy and adapt them for each document's specific sections and tables.

---

## Error Handling

- If handwriting is illegible in a region: insert `[illegible]` placeholder and note it
- If a diagram is ambiguous: reconstruct the most faithful interpretation and add a comment `<!-- Note: diagram reconstructed from ambiguous sketch -->`
- If a page is blank or nearly blank: skip it silently
- If input has no diagrams: still produce all three outputs, just omit the Diagrams sheet from Excel

---

## Example Trigger Phrases

- "turn my handwritten notes into a doc"
- "digitize this PDF scan"
- "convert this image of notes to markdown and excel"
- "OCR this and make it clean"
- "my notes have diagrams, convert them"
- "make a professional document from my scan"
- *(user uploads image/PDF with no explanation — check if it contains handwriting and ask)*
