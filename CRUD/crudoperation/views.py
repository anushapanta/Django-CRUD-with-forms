from django.shortcuts import render, redirect
from .models import StudentDetails
from .forms import StudentForm

# Create your views here.


def studentListDetails(request):
    students = StudentDetails.objects.all()
    return render(request, "student_template/student_list.html", {'students': students})


def studentCreate(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('student_template/student_list')
            except:
                pass
    else:
        form = StudentForm()
    return render(request, 'student_template/student_create.html', {'form': form})


def studentUpdate(request, id):
    student = StudentDetails.objects.get(id=id)
    form = StudentForm(initial={'firstname': student.firstname,
                                'lastname': student.lastname, 'address': student.address, 'dob': student.date,
                                'phone': student.phone, 'image': student.image, 'faculty': student.faculty})
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            try:
                form.save()
                model = form.instance
                return redirect('student_template/student_list')
            except Exception as e:
                pass
    return render(request, 'student_template/student_update.html', {'form': form})


def studentDelete(request, id):
    student = StudentDetails.objects.get(id=id)
    try:
        student.delete()
    except:
        pass
    return redirect('student_template/student_list')
