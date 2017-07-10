from django.shortcuts import render
from .forms import QuadraticFrom


def quadratic_result(request):
    flag = False
    if request.GET:
        form = QuadraticFrom(request.GET)
        if form.is_valid():
            a = form.cleaned_data['a']
            if a == 0:
                flag = True
            #     raise forms.ValidationError('A koeff should not equals zero')
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            return render(request, 'quadratic/quadratic.html', {'form': form,
                                                                'dis': __dis(a, b, c),
                                                                'roots': __calc_roots(a, b, c),
                                                                'is_zero': flag})
    else:
        form = QuadraticFrom()
    return render(request, 'quadratic/quadratic.html', {'form': form})


def __dis(a, b, c):
    return b ** 2 - 4 * a * c


def __calc_roots(a, b, c):
    d = __dis(a, b, c)
    if d >= 0:
        return ((-b - d**0.5) * a / 2, (- b + d**0.5) * a / 2)
