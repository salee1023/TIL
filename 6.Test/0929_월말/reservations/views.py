from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Reservation, Comment
from .forms import ReservationForm, CommentForm 

# Create your views here.
@login_required
def create(request):
    # Q2-1
    # POST 요청이면 예약을 저장한다.
    if request.method =="POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation = form.save()
            return redirect('reservations:detail', reservation.pk)
    # GET요청이면, 예약글을 작성한다.
    else:
        form = ReservationForm()
    context = {
        'form': form,
    }
    return render(request, 'reservations/create.html', context)
    


@login_required
def index(request):
    # Q2-2     
    # 관리자 계정일 때
    if request.user.is_staff == 1:   
        reservations = Reservation.objects.all()
    # 관리자가 아니면 본인이 작성한 글만 조회
    else:
        reservations = request.user.reservation_set.all()
    context = {
            'reservations': reservations,
        }
    return render(request, 'reservations/index.html', context)

    
@login_required
def detail(request, pk):
    # Q2-3
    # 존재하지 않는 글을 조회하면, 404페이지 반환
    reservation = get_object_or_404(Reservation,pk=pk)
    comment_form = CommentForm()
    # 해당 글의 작성자, 관리자만 예약 내역 조회
    if request.user == reservation.user or request.user.is_staff == 1:
        context = {
            'reservation': reservation,
            'comment_form': comment_form,
        }
        return render(request, 'reservations/detail.html', context)
    # 관리자나 작성자가 아니면 redirect
    else:
        return redirect('reservations:index')


@login_required
@require_POST
def comments_create(request, pk):
    # Q3-1
    form = CommentForm(request.POST)
    reservation = Reservation.objects.get(pk=pk)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.reservation = reservation
        comment = form.save()
    return redirect('reservations:detail', pk)
   