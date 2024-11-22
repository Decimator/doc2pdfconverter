from rest_framework import serializers

class DocxUploadSerializer(serializers.Serializer):
    docx_file = serializers.FileField()
    pdf_password = serializers.CharField(
        required=False, 
        write_only=True, 
        style={'input_type': 'password'}
    )