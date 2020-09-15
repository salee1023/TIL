# 0914_homework

#### 1. Django Model Form

```python
# models.py
class Reservation(models.Model):
    name = models.CharField(max_length=10)
    date = models.DateField()
```

```python
from django import forms
from .models import Reservation

class ReservationForm(____(a)____):
    
    class ___(b)___:
        model = Reservation
        field = '__all__'
```

(a) : forms.ModelForm

(b) : Meta

---

```python
def create(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect('reservations:detail', reservation.pk)
    else:
        form = ReservationForm()
        context = {
            'form': form,
        }
    	return render(request, 'reservations/create.html', context)
```

👉 만약, http method가 `POST`이지만 유효성 검증을 통과하지 못했을 경우, return 해줄 context가 없기 때문에 오류가 난다. 

따라서 context ~return을  if-else와 동일한 선상으로 바꿔줘야한다.

---

```python
def update(request, pk):
    reservation = Reservation.objects.get(pk=pk)
    if request.method == 'POST': 
        ___(a)___
        if form.is_valid():
            reservation = form.save()
            return redirect('reservations:detail', reservation.pk)
    else: 
        ___(b)___
    context = {
        'reservation' : reservation,
        'form': form,
    }
    return render(request, 'reservations/update.html', context)
```

(a) : form = ReservationForm(request.POST, instance=reservation)

(b) : form = ReservationForm(instance=reservation)

---

```html
<h2>edit</h2>
<form action="{% url 'reservations:update' reservation.pk %}" method="POST">
	{% csrf_token %}
    {{ form.__(a)__ }}
    <input type="submit" value="submit">                                       
</form>
```

(a) : as_p, as_table, as_ul







