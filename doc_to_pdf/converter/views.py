from django.shortcuts import render
from django.http import FileResponse, HttpResponse
from .forms import DocxUploadForm
from .utils import convert_docx_to_pdf
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .serializer import DocxUploadSerializer
from PyPDF2 import PdfWriter, PdfReader
from io import BytesIO

from django.utils.timezone import now  # To get current time

def docx_to_pdf_view(request):
    metadata = {}  # Dictionary to store file metadata

    if request.method == 'POST':
        form = DocxUploadForm(request.POST, request.FILES)
        if form.is_valid():
            docx_file = request.FILES['docx_file']
            pdf_password = request.POST.get('pdf_password', '')

            # Extract metadata
            metadata['file_name'] = docx_file.name
            metadata['file_size'] = docx_file.size
            metadata['uploaded_at'] = now().strftime("%Y-%m-%d %H:%M:%S")  # Current timestamp

            try:
                # Convert DOCX to PDF
                pdf_buffer = convert_docx_to_pdf(docx_file)

                # Add password protection if a password is provided
                if pdf_password:
                    pdf_buffer = add_pdf_password(pdf_buffer, pdf_password)

                # Serve the PDF as a file response
                return FileResponse(
                    pdf_buffer,
                    as_attachment=True,
                    filename='converted.pdf'
                )
            except Exception as e:
                return render(request, 'upload.html', {
                    'form': form,
                    'error': f"Conversion failed: {str(e)}",
                })

    else:
        form = DocxUploadForm()

    return render(request, 'upload.html', {'form': form, 'metadata': metadata})


class DocxToPdfAPIView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = DocxUploadSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            docx_file = serializer.validated_data['docx_file']
            pdf_password = request.data.get('pdf_password', '')
            
            try:
                
                pdf_buffer = convert_docx_to_pdf(docx_file)
                
                
                if pdf_password:
                    pdf_buffer = add_pdf_password(pdf_buffer, pdf_password)
                
                response = HttpResponse(
                    pdf_buffer.getvalue(),
                    content_type='application/pdf'
                )
                response['Content-Disposition'] = 'attachment; filename=converted.pdf'
                return response
            
            except Exception as e:
                return HttpResponse(
                    f"Conversion error: {str(e)}",
                    status=400
                )
        
        return HttpResponse(
            str(serializer.errors),
            status=400
        )

def add_pdf_password(pdf_buffer, password):
   
    
    pdf_writer = PdfWriter()
    
    
    pdf_reader = PdfReader(pdf_buffer)
    
   
    for page in pdf_reader.pages:
        pdf_writer.add_page(page)
    
   
    pdf_writer.encrypt(password)
    
    
    output_buffer = BytesIO()
    pdf_writer.write(output_buffer)
    output_buffer.seek(0)
    
    return output_buffer
