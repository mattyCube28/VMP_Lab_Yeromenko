import urllib.request
import json
import csv  
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def import_csv(request):
    if request.method == 'POST' and request.FILES.get('csv_file'):
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith('.csv'):
            return HttpResponse("Будь ласка, завантажте файл у форматі CSV.")
            
        file_data = csv_file.read().decode('utf-8').splitlines()
        reader = csv.reader(file_data)
        next(reader) 
        
        for row in reader:
            Student.objects.create(
                full_name=row[0],
                group=row[1],
                math_grade=int(row[2]),
                programming_grade=int(row[3]),
                english_grade=int(row[4])
            )
        return redirect('student_list')
        
    return render(request, 'students/import_csv.html')

def student_report(request):
    students = Student.objects.all()
    names = [student.full_name for student in students]
    math_grades = [student.math_grade for student in students]
    context = {
        'names': names,
        'math_grades': math_grades,
    }
    return render(request, 'students/report.html', context)

def import_api(request):
    if request.method == 'POST':
        api_url = "https://jsonplaceholder.typicode.com/users"
        
        try:
            response = urllib.request.urlopen(api_url)
            data = json.loads(response.read())
            for item in data:
                Student.objects.create(
                    full_name=item.get('name', 'Невідомий'),
                    group=item.get('company', {}).get('name', 'Невідома група'),
                    math_grade=85,
                    programming_grade=90,
                    english_grade=88,
                    contact_info=item.get('email', '')
                )
            return redirect('student_list') 
        except Exception as e:
            from django.http import HttpResponse
            return HttpResponse(f"Сталася помилка при завантаженні з API: {e}")

    return render(request, 'students/import_api.html')