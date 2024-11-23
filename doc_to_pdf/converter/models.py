from django.db import models

class Document(models.Model):
    pdf_doc = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Document {self.id} - {self.pdf_doc.name}"
    
    def get_metadata(self):
        return {
            "file_name": self.doc_file.name,
            "file_size": self.doc_file.size,
            "uploaded_at": self.uploaded_at,
        }

