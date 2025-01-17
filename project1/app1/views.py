from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def stu_view(request):
    form = StudentForm()
    print(request.POST)
    if(request.method == 'POST'):
        form = StudentForm(request.POST)
        if(form.is_valid()):
            form.save()
    template_name = 'app1/student_form.html'
    context = {'form':form}
    return render(request, template_name, context)