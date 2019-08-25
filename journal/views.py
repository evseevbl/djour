from django.shortcuts import render
from journal.models import Student, Squad
from journal.manager import StudentsManager



# Create your views here.
def index(request):
    ctx = {"user": "Boris"}

    return render(
        request,
        "journal/index.html",
        ctx.update(
            {
                # "user_id": user_id,
            }
        )
    )



def students(request):
    # manager = StudentsManager()
    # students = manager.get_students_by_squad('1702')
    # q = Student.objects.filter(squad=Squad(code='1702'))
    ls: [Student] = Student.objects.all()
    # filter(squad='1702')
    for elem in ls:
        print(elem)

    return render(
        request,
        "journal/students.html",
        {
            # "user_id": user_id,
            "students": ls,
        }
    )
