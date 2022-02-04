from django.http import HttpResponse
from .models import Recruit
from django.shortcuts import render, get_object_or_404, redirect
from .forms import RecruitForm
from django.contrib import messages

# Create your views here.

def recruit(request):

    recruit_list = Recruit.objects.order_by('-create_date')
    context = {'recruit_list': recruit_list}
    return render(request, 'recruitment/recruit.html', context)

def detail(request, recruit_id):
    recruit = get_object_or_404(Recruit, pk=recruit_id)
    context = {'recruit': recruit}
    return render(request, 'recruitment/recruit_detail.html', context)

def recruit_create(request):
    if request.method == 'POST':
        form = RecruitForm(request.POST)
        if form.is_valid():
            recruit = form.save(commit=False)
            recruit.save()
            return redirect('recruitment:recruit')
    else:
        form = RecruitForm()
    context = {'form': form}
    return render(request, 'recruitment/recruit_form.html', context)

def vote_recruit(request, recruit_id):
    recruit = get_object_or_404(Recruit, pk=recruit_id)
    if recruit.present_num == recruit.max_num:
        messages.warning(request, '마감되었습니다')
    else:
        recruit.present_num += 1
        recruit.save()
        messages.info(request, '예약되었습니다')
    return redirect('recruitment:detail', recruit_id=recruit.id)

