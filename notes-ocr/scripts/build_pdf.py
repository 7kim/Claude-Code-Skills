"""
notes-ocr / build_pdf.py
Reusable PDF builder for digitized handwritten notes.

Usage (standalone):
    python build_pdf.py --data structured_data.json --out output.pdf

Or import and call build_pdf(data, output_path) directly.

Uses the same data dict as build_excel.py (see that file for schema).
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.lib.units import inch
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, PageBreak,
        Table, TableStyle, HRFlowable, KeepTogether
    )
except ImportError:
    sys.exit("reportlab not found — run: pip install reportlab --break-system-packages")


# ── Color palette ─────────────────────────────────────────────────────────────
BLUE_DARK   = colors.HexColor("#366092")
BLUE_MID    = colors.HexColor("#4472C4")
BLUE_LIGHT  = colors.HexColor("#B4C7E7")
BLUE_PALE   = colors.HexColor("#EEF3FA")
GREY_TEXT   = colors.HexColor("#595959")
WHITE       = colors.white
BLACK       = colors.black
ROW_ALT     = colors.HexColor("#F0F4FA")


# ── Table style helper ────────────────────────────────────────────────────────
def _table_style(n_header_rows=1):
    return TableStyle([
        ("BACKGROUND",  (0, 0), (-1, n_header_rows - 1), BLUE_DARK),
        ("TEXTCOLOR",   (0, 0), (-1, n_header_rows - 1), WHITE),
        ("FONTNAME",    (0, 0), (-1, n_header_rows - 1), "Helvetica-Bold"),
        ("FONTSIZE",    (0, 0), (-1, n_header_rows - 1), 9),
        ("ALIGN",       (0, 0), (-1, -1), "LEFT"),
        ("VALIGN",      (0, 0), (-1, -1), "TOP"),
        ("FONTNAME",    (0, n_header_rows), (-1, -1), "Helvetica"),
        ("FONTSIZE",    (0, n_header_rows), (-1, -1), 9),
        ("ROWBACKGROUNDS", (0, n_header_rows), (-1, -1), [WHITE, ROW_ALT]),
        ("GRID",        (0, 0), (-1, -1), 0.5, colors.HexColor("#CCCCCC")),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING",    (0, 0), (-1, -1), 6),
        ("LEFTPADDING",   (0, 0), (-1, -1), 8),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 8),
    ])


# ── Page template (header + footer) ──────────────────────────────────────────
class _PageTemplate:
    def __init__(self, title):
        self.title = title

    def __call__(self, canvas, doc):
        canvas.saveState()
        w, h = letter

        # Header bar
        canvas.setFillColor(BLUE_DARK)
        canvas.rect(0, h - 0.45 * inch, w, 0.45 * inch, fill=1, stroke=0)
        canvas.setFillColor(WHITE)
        canvas.setFont("Helvetica-Bold", 10)
        canvas.drawString(0.5 * inch, h - 0.3 * inch, self.title)

        # Footer bar
        canvas.setFillColor(BLUE_PALE)
        canvas.rect(0, 0, w, 0.35 * inch, fill=1, stroke=0)
        canvas.setFillColor(GREY_TEXT)
        canvas.setFont("Helvetica", 8)
        canvas.drawString(0.5 * inch, 0.12 * inch,
                          f"Generated {datetime.now().strftime('%B %d, %Y')}")
        canvas.drawRightString(w - 0.5 * inch, 0.12 * inch, f"Page {doc.page}")

        canvas.restoreState()


def build_pdf(data: dict, output_path: str):
    title  = data.get("title", "Document")
    author = data.get("author", "")
    date   = data.get("date", "")

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=0.75 * inch, rightMargin=0.75 * inch,
        topMargin=0.75 * inch,  bottomMargin=0.6 * inch,
        title=title,
        author=author,
    )

    styles = getSampleStyleSheet()

    # ── Custom styles ─────────────────────────────────────────────────────────
    S = {
        "title": ParagraphStyle("DocTitle",
            fontSize=28, textColor=BLUE_DARK, alignment=TA_CENTER,
            fontName="Helvetica-Bold", spaceAfter=8),
        "subtitle": ParagraphStyle("DocSubtitle",
            fontSize=14, textColor=BLUE_MID, alignment=TA_CENTER,
            fontName="Helvetica", spaceAfter=6),
        "meta": ParagraphStyle("DocMeta",
            fontSize=10, textColor=GREY_TEXT, alignment=TA_CENTER,
            fontName="Helvetica"),
        "abstract": ParagraphStyle("DocAbstract",
            fontSize=10, textColor=BLACK, alignment=TA_JUSTIFY,
            fontName="Helvetica", leftIndent=30, rightIndent=30,
            spaceAfter=6, leading=15),
        "section": ParagraphStyle("Section",
            fontSize=14, textColor=WHITE, fontName="Helvetica-Bold",
            spaceBefore=4, spaceAfter=4,
            backColor=BLUE_DARK, leftIndent=-6, rightIndent=-6,
            borderPadding=(6, 8, 6, 8)),
        "subsection": ParagraphStyle("Subsection",
            fontSize=11, textColor=BLUE_DARK, fontName="Helvetica-Bold",
            spaceBefore=10, spaceAfter=4),
        "body": ParagraphStyle("Body",
            fontSize=10, fontName="Helvetica", leading=14,
            spaceAfter=6, alignment=TA_JUSTIFY),
        "bullet": ParagraphStyle("Bullet",
            fontSize=10, fontName="Helvetica", leading=14,
            spaceAfter=3, leftIndent=16, bulletIndent=6),
        "toc_item": ParagraphStyle("TOCItem",
            fontSize=11, fontName="Helvetica", spaceAfter=4, leftIndent=16),
        "diagram_box": ParagraphStyle("DiagramBox",
            fontSize=10, fontName="Helvetica-Bold", textColor=BLUE_DARK,
            backColor=BLUE_PALE, leftIndent=12, borderPadding=8,
            spaceAfter=4),
        "diagram_note": ParagraphStyle("DiagramNote",
            fontSize=9, fontName="Helvetica-Oblique", textColor=GREY_TEXT,
            leftIndent=12, spaceAfter=10),
    }

    elements = []
    on_page = _PageTemplate(title)

    # ══════════════════════════════════════════════════════════════════════════
    # TITLE PAGE
    # ══════════════════════════════════════════════════════════════════════════
    elements.append(Spacer(1, 1.4 * inch))
    elements.append(Paragraph(title, S["title"]))
    elements.append(Spacer(1, 0.15 * inch))

    meta_parts = []
    if author: meta_parts.append(f"<b>Author:</b> {author}")
    if date:   meta_parts.append(f"<b>Date:</b> {date}")
    if meta_parts:
        elements.append(Paragraph("  |  ".join(meta_parts), S["meta"]))

    elements.append(Spacer(1, 0.5 * inch))
    elements.append(HRFlowable(width="60%", color=BLUE_LIGHT, thickness=2))
    elements.append(Spacer(1, 0.4 * inch))

    # Abstract / description from first section if available
    sections = data.get("sections", [])
    if sections and sections[0].get("description"):
        abstract = sections[0]["description"]
        elements.append(Paragraph(abstract, S["abstract"]))

    elements.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # TABLE OF CONTENTS
    # ══════════════════════════════════════════════════════════════════════════
    elements.append(Paragraph("Table of Contents", S["section"]))
    elements.append(Spacer(1, 0.2 * inch))

    for i, sec in enumerate(sections, 1):
        elements.append(Paragraph(f"{i}.  {sec.get('name', '')}", S["toc_item"]))

    elements.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # SECTIONS
    # ══════════════════════════════════════════════════════════════════════════
    for sec_idx, sec in enumerate(sections, 1):
        sec_name = sec.get("name", f"Section {sec_idx}")
        block = []

        # Section heading
        block.append(Paragraph(f"{sec_idx}.  {sec_name}", S["section"]))
        block.append(Spacer(1, 0.1 * inch))

        # Prose description
        if sec.get("description"):
            block.append(Paragraph(sec["description"], S["body"]))
            block.append(Spacer(1, 0.1 * inch))

        # Key-value fields → two-column table
        fields = sec.get("fields", [])
        if fields:
            block.append(Paragraph("Details", S["subsection"]))
            tbl_data = [["Field", "Value"]] + [[f["label"], f["value"]] for f in fields]
            tbl = Table(tbl_data, colWidths=[2.0 * inch, 4.5 * inch])
            tbl.setStyle(_table_style())
            block.append(tbl)
            block.append(Spacer(1, 0.2 * inch))

        # Structured tables
        for tbl_meta in sec.get("tables", []):
            tbl_title = tbl_meta.get("title", "")
            headers = tbl_meta.get("headers", [])
            rows = tbl_meta.get("rows", [])

            if tbl_title:
                block.append(Paragraph(tbl_title, S["subsection"]))

            if headers or rows:
                tbl_data = ([headers] if headers else []) + rows
                n_cols = max(len(r) for r in tbl_data) if tbl_data else 1
                col_w = 6.5 * inch / n_cols
                tbl = Table(tbl_data, colWidths=[col_w] * n_cols)
                tbl.setStyle(_table_style(1 if headers else 0))
                block.append(tbl)

            block.append(Spacer(1, 0.2 * inch))

        # Diagram references
        for diag in sec.get("diagrams", []):
            block.append(Paragraph(
                f"📊  Diagram: {diag.get('name', 'Diagram')}",
                S["diagram_box"]
            ))
            if diag.get("description"):
                block.append(Paragraph(diag["description"], S["body"]))
            block.append(Paragraph(
                "→ Full Mermaid diagram available in the Markdown (.md) file",
                S["diagram_note"]
            ))

        elements.extend(block)
        elements.append(PageBreak())

    # ══════════════════════════════════════════════════════════════════════════
    # BUILD
    # ══════════════════════════════════════════════════════════════════════════
    doc.build(elements, onFirstPage=on_page, onLaterPages=on_page)
    print(f"✅ PDF saved: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Build PDF from structured notes data")
    parser.add_argument("--data", required=True, help="Path to structured_data.json")
    parser.add_argument("--out",  required=True, help="Output .pdf path")
    args = parser.parse_args()

    with open(args.data) as f:
        data = json.load(f)

    build_pdf(data, args.out)


if __name__ == "__main__":
    main()
