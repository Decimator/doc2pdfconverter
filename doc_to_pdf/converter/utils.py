import io
from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def convert_docx_to_pdf(docx_file):
   
    pdf_buffer = io.BytesIO()
    pdf_canvas = canvas.Canvas(pdf_buffer, pagesize=letter)
  
    pdf_canvas.setFont("Helvetica", 12)
    
    doc = Document(docx_file)
    
    y_position = 720  
    margin = 50
    
    
    for para in doc.paragraphs:
        text = para.text
        
        if y_position < 50:
            pdf_canvas.showPage()
            y_position = 720
        
        try:
           
            pdf_canvas.drawString(margin, y_position, text)
        except Exception as e:
            
            pdf_canvas.drawString(margin, y_position, "[Unrenderable Text]")
        
        y_position -= 15
    
    
    pdf_canvas.save()
    pdf_buffer.seek(0)
    return pdf_buffer
