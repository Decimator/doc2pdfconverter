from django import forms

class DocxUploadForm(forms.Form):
    docx_file = forms.FileField()
    pdf_password = forms.CharField(
        widget=forms.PasswordInput(), 
        required=False, 
        help_text="Optional: Protect your PDF with a password"
    )