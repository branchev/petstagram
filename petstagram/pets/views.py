from django.shortcuts import render, redirect

from petstagram.common.forms import CommentForm
from petstagram.common.models import Comment
from petstagram.pets.models import Pet, Like
from petstagram.pets.forms import PetCreateForm, PetEditForm


def list_pets(request):
    all_pets = Pet.objects.all()

    context = {
        "pets": all_pets
    }

    return render(request, 'pets/pet_list.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)

    # MONKEY TYPING ON THE ROW BELOW
    pet.likes_count = pet.like_set.count()

    context = {
        "pet": pet,
        'comment_form': CommentForm(),
        'comments': pet.comment_set.all(),
    }

    return render(request, 'pets/pet_detail.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(
        pet=pet,
    )
    like.save()

    return redirect('pet details', pet.id)


def create_pet(request):
    if request.method == 'GET':
        context = {
            'form': PetCreateForm()
        }
        return render(request, 'pets/pet_create.html', context)
    else:
        form = PetCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list pets')


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'form': PetEditForm(instance=pet),
            'pet': pet,
        }
        return render(request, 'pets/pet_edit.html', context)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('list pets')
    return redirect('list pets')


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        context = {
            'pet': pet,
        }
        return render(request, 'pets/pet_delete.html', context)
    else:
        pet.delete()
        return redirect('list pets')


def comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        # comment = Comment(
        #     comment=form.comment,
        #     pet=pet,
        # )
        # comment.save()
        form.save()
    return redirect('pet details')
