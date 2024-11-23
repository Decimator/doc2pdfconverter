import io
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.units import inch

def convert_docx_to_pdf(docx_file):
    
    doc = Document(docx_file)
    
    
    pdf_buffer = io.BytesIO()
    pdf = SimpleDocTemplate(
        pdf_buffer,
        pagesize=letter,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18,
    )
    
    
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    bold_style = ParagraphStyle('Bold', parent=normal_style, fontName='Helvetica-Bold')
    italic_style = ParagraphStyle('Italic', parent=normal_style, fontName='Helvetica-Oblique')
    centered_style = ParagraphStyle('Centered', parent=normal_style, alignment=TA_CENTER)
    right_style = ParagraphStyle('Right', parent=normal_style, alignment=TA_RIGHT)
    
    
    story = []
    
    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue  
        
        
        formatted_text = ""
        for run in para.runs:
            run_text = run.text.replace("\n", "<br />")
            if run.bold:
                run_text = f"<b>{run_text}</b>"
            if run.italic:
                run_text = f"<i>{run_text}</i>"
            formatted_text += run_text
        
       
        if para.alignment == 1:  
            style = centered_style
        elif para.alignment == 2:  
            style = right_style
        else: 
            style = normal_style
        
        
        story.append(Paragraph(formatted_text, style))
        story.append(Spacer(1, 0.2 * inch))
    
    
    pdf.build(story)
    pdf_buffer.seek(0)
    
    
    return pdf_buffer
