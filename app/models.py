from django.db import models

# Create your models here.
from django.db import models
from django import forms

class Resume(models.Model):
    resume        = models.FileField('Upload Resumes', upload_to='resumes/')
    name          = models.CharField('Name', max_length=255, null=True, blank=True)
    email         = models.CharField('Email', max_length=255, null=True, blank=True)
    mobile_number = models.CharField('Mobile Number',  max_length=255, null=True, blank=True)
    education     = models.CharField('Education', max_length=255, null=True, blank=True)
    skills        = models.CharField('Skills', max_length=1000, null=True, blank=True)
    company_name  = models.CharField('Company Name', max_length=1000, null=True, blank=True)
    college_name  = models.CharField('College Name', max_length=1000, null=True, blank=True)
    designation   = models.CharField('Designation', max_length=1000, null=True, blank=True)
    experience    = models.CharField('Experience', max_length=1000, null=True, blank=True)
    uploaded_on   = models.DateTimeField('Uploaded On', auto_now_add=True)
    total_experience  = models.CharField('Total Experience (in Years)', max_length=1000, null=True, blank=True)


    def __str__(self):
            return str(self.name)

class UploadResumeModelForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['resume']
        widgets = {
            'resume': forms.ClearableFileInput(attrs={'allow_multiple_selected': False}),
        }