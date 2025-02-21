from django.shortcuts import render, redirect
from .models import News, Car, Color, Category, Student

def news_create_view(request):
    
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']

        news = News(title=title, description=description)
        news.save()

    return render(request, template_name='app/news_create.html')

def car_create_view(request):

    categories = Category.objects.all()
    colors = Color.objects.all()

    if request.method == 'POST':
        title = request.POST['title']
        model = request.POST['model']
        year = request.POST['year']
        odometer = request.POST['odometer']
        engine_capacity = request.POST['engine_capacity']
        color_id = request.POST['color_id']
        category_id = request.POST['category_id']
        image = request.FILES['image']

        category = Category.objects.get(id=category_id)
        color = Color.objects.get(id=color_id)

        car = Car(title=title, category=category, model=model, year=year, odometer=odometer,
                  engine_capacity=engine_capacity, color=color, image=image)
        
        car.save()

        return redirect('news_create')

    return render(request, 'app/car_create.html', context={"categories":categories, "colors":colors})

def student_registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']

        student = Student(name=name, age=age, email=email)
        student.save()

        return redirect('student_registration')

    return render(request, 'app/student_registration.html')