from django.shortcuts import render
from .models import *


def index(request):
    branches = Branches.objects.all()
    context = {
        'branches': branches,
        'title': 'Структура Центра',
    }
    return render(request, 'structure/index.html', context=context)


def view_branch(request, branch_id):
    branches_item = Branches.objects.get(pk=branch_id)
    image_title = GalleryBranches.objects.all().filter(in_the_cont=1, keyBranches=branch_id)
    image = GalleryBranches.objects.all().filter(keyBranches=branch_id)
    image_map = GalleryBranches.objects.all().filter(location_map=1, keyBranches=branch_id)
    specialists = Specialists.objects.all().filter(keyBranches=branch_id)
    return render(request, 'structure/view_branches.html', {"branches_item": branches_item, 'image': image, 'image_title': image_title, 'image_map': image_map,
                                                            "specialists": specialists})

