from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Report
from django.utils import timezone
from .forms import ReportForm

def index(request):
    # report 목록 출력
    report_list=Report.objects.order_by('-create_date')
    context={'report_list':report_list}
    return render(request, 'report/report_list.html',context)


def detail(request,report_id):
    # report 내용 출력
    report =get_object_or_404(Report,pk=report_id)
    context={'report':report}
    return render(request,'report/report_detail.html',context)

def answer_create(request,report_id):
    report=get_object_or_404(Report, pk=report_id)
    report.answer_set.create(content=request.POST.get('content'),
                             create_date=timezone.now())
    return redirect('report:detail',report_id=report.id)


def report_create(request):
    if request.method == "POST":
        form=ReportForm(request.POST)
        if form.is_valid():
            report=form.save(commit=False)
            report.create_date=timezone.now()
            report.save()
            return redirect('report:index')
    else:
        form=ReportForm()
    context={'form':form}
    return render(request, 'report/report_form.html',context)