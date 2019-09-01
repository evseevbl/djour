from django.shortcuts import render
from journal.models import Student, Squad, Mark
from journal.manager import StudentsManager



# Create your views here.
def index(request):
    name = "boris"
    if request.GET.get('mybtn'):
        name = str(request.GET.get('mytextbox'))

    return render(
        request,
        "journal/index.html",
        {
            "user": name
        }
    )



def students(request):
    # manager = StudentsManager()
    # students = manager.get_students_by_squad('1702')
    # q = Student.objects.filter(squad=Squad(code='1702'))
    ls: [Student] = Student.objects.filter(squad__code="1702")
    # # filter(squad='1702')
    for elem in ls:
        print(elem)
    # ls = []
    return render(
        request,
        "journal/students.html",
        {
            # "user_id": user_id,
            "students": ls,
        }
    )



def test(request):
    return render(request, "journal/index.html")



def marks_base(request):
    marks = Mark.objects.all()
    return render(
        request,
        "journal/marks/base.html",
        {
            "marks": marks
        }
    )



def marks_squad(request, squad_code="999"):
    print(request, squad_code)

    marks = Mark.objects.filter(student__squad__code=squad_code).prefetch_related(
        'student__mark_set',
        'student__squad__student_set',
    )

    return render(
        request,
        "journal/marks/base.html",
        {
            "marks": marks
        }
    )
