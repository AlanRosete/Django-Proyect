from django.forms import ModelForm
from .models import Employee

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        #exclude = ("email,") ESTO PARA REALIZAR LA MUESTRA DE TODOS EXCEPTO:
        fields =  "__all__" #["name","last_name","email"] Se realizan todos sin irlos poniendo 1x1
