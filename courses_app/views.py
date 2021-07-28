from django.contrib import messages
from courses_app.models import Course, Description,Comment
from django.shortcuts import redirect, render

# Create your views here.
def main_view(request):
    context={"all_courses":Course.objects.all()}
    return render(request,'courses.html',context)

def create(request):
    if request.method=="POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
        # redirect the user back to the form to fix the errors
            return redirect('/')
        else:
            Description.objects.create(course_description=request.POST["course_description"],course=Course.objects.create(course_name=request.POST["course_name"]))
            return redirect('/')

def destroy(request,id):
    if 'no_delete' in request.POST:
        return redirect('/')
    if 'yes_delete' in request.POST:
        Course.objects.get(id=id).delete()
        return redirect('/')
    context={"this_course":Course.objects.get(id=id)}
    return render(request,'course_details.html',context)

def comment(request,id):
    context={"all_comments":Comment.objects.filter(course=Course.objects.get(id=id)),
    "course_id":id}
    if 'add_comments' in request.POST:
        Comment.objects.create(course_comment=request.POST["course_comments"],course=Course.objects.get(id=id))
    return render(request,'comments.html',context)

        