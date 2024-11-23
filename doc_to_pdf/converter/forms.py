from django import forms

class DocxUploadForm(forms.Form):
    docx_file = forms.FileField(
        label="Choose DOCX File", 
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control', 
            'id': 'docx_file', 
            'accept': '.doc,.docx,.docm', 
            'required': True
        }),
        help_text="Supported formats: .doc, .docx, .docm"
    )

    pdf_password = forms.CharField(
        label="PDF Password (Optional)", 
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Enter password (Optional)'
        }),
        required=False, 
        
    )
