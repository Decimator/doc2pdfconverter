from django.urls import path
from .views import DocxToPdfAPIView, docx_to_pdf_view

urlpatterns = [
    path('convert/', docx_to_pdf_view, name='docx_to_pdf'),
    path('api/convert', DocxToPdfAPIView.as_view(), name='docx_to_pdf_api'),
]
