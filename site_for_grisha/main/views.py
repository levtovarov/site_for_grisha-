from django.shortcuts import render, redirect
from django.views.decorators import csrf

from .models import *
import fuzzywuzzy.fuzz as fz
from fuzzywuzzy import process
from .forms import GroupSearch, CoverSearch, CoverUpload
import re

need_list = []
a = r'\\'


@csrf.csrf_protect
def index(request):
    group_list = [i.title for i in Rock.objects.all()]
    # data = {'hr_1': r'/about_us'}
    # data1 = {i: j for i, j in enumerate(group_list)}
    submitbutton = request.POST.get("submit")
    group_name = ''
    form = GroupSearch(request.POST)
    if form.is_valid():
        group_name = form.cleaned_data.get("group_name")
    group_name = re.sub('\W\D\s,', ' ', group_name)
    need_list = [i[0] for i in process.extract(group_name, group_list, limit=10) if i[1] > 50]
    data = {'need_list': need_list, 'form': form, 'zip': list(
        zip(need_list, [f'https://ru.wikipedia.org/wiki/{re.sub(" +", "_", i)}' for i in need_list],
            range(70, 70 + len(need_list) * 17, 17)))}
    print(data['zip'])
    return render(request, r'main\index.html', context=data)


def songs(request):
    return render(request, r'main\songs.html')


def info(request):
    return render(request, r'main\info.html')


def about_us(request):
    return render(request, r'main\about_us.html')


@csrf.csrf_protect
def forum(request):
    print(Cover.objects.all())
    covers = [[i.title, i.creator, i.file.name.split(fr'{a[0]}')[-1]] for i in Cover.objects.all()]
    print(covers)
    cover_for_search = ''
    form = CoverSearch(request.POST)
    if form.is_valid():
        try:
            cover_for_search = form.cleaned_data.get('cover_name')
        except Exception as e:
            print('Хуйня какая то')
            print(e)

    cover_for_search = re.sub('\W\D\s,', ' ', cover_for_search)
    need_list_title = [(i, j) for i, j in
                       enumerate(process.extract(cover_for_search, [j[0] for j in covers], limit=10))]
    # pre_need_list = [i[1] for i in need_list_title]
    need_list = [i[1][0] for i in need_list_title if i[1][1] > 50]
    need_list_indexes = [i[0] for i in need_list_title if i[1][1] > 50]
    # print(need_list_indexes)
    need_list_audies = [covers[i][2] for i in need_list_indexes]
    # print(need_list_audies)
    zip_list = list(zip(need_list, range(90, len(need_list) * 17 + 90, 17), need_list_audies))
    data = {'form': form, 'need_list': need_list,
            'zip': zip_list, 'zip2': zip_list}
    print(list(data['zip']))

    return render(request, r'main\forum.html', context=data)


@csrf.csrf_protect
def cover_upload(request):
    form = CoverUpload(request.POST, request.FILES)
    covers = [[i.title, i.creator, i.file.name.split(fr'{a[0]}')[-1]] for i in Cover.objects.all()]
    if form.is_valid():
        try:
            if form.cleaned_data.get("title") is not None and form.cleaned_data.get(
                    "creator") is not None and form.cleaned_data.get("file") is not None and (
                    form.cleaned_data.get("title") not in [i[0] for i in covers] and form.cleaned_data.get(
                    "creator") not in [i[1] for i in covers]):
                form.save()
                print(form.cleaned_data.get("title"))
                print(form.cleaned_data.get("creator"))
                print(form.cleaned_data.get("file"))

        except Exception as e:
            print('Хуйня какая то')
            print(e)

    data = {'form': form}
    covers = [[i.title, i.creator, i.file.name.split(fr'{a[0]}')[-1]] for i in Cover.objects.all()]
    return render(request, r'main\cover_upload.html', context=data)
