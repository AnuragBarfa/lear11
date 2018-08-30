from django.core.exceptions import ValidationError
def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    #whenever edit here also edit the list in add_notes.html file
    valid_extensions = ['.pdf', '.doc', '.docx','.xlsx', '.xls','.odt',
                        '.jpg', '.png','.jpeg',
                        '.py','.cpp','.c','.r','.m'
                        ]
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')