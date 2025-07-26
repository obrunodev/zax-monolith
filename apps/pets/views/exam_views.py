from apps.pets.models import Exam, Pet
from apps.pets.forms import ExamForm
from django.shortcuts import get_object_or_404, redirect, render


def upload_exam(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    if request.method == 'POST':
        form = ExamForm(request.POST, request.FILES)
        if form.is_valid():
            exam = form.save(commit=False)
            exam.pet = pet
            exam.save()
            print('Deu tudo certo com o formulário e o exame foi salvo!')
            return redirect('pets:list')
        else:
            print(f'Alguma coisa deu errado: {form.errors}.')
    else:
        form = ExamForm()
    
    context = {
        'form': form,
        'pet': pet,
    }
    return render(request, 'pets/exam_form.html', context)
