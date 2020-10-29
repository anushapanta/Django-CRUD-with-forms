from django.forms import ModelForm
from .models import StudentDetails

class StudentForm(ModelForm):
    class Meta:
        model = StudentDetails
        fields = '__all__'