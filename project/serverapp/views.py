from django.shortcuts import render

def power_calculator(request):
    intensity = ''
    resistance = ''
    power = ''

    if request.method == 'POST':
        try:
            intensity = float(request.POST.get('intensity', 0))
            resistance = float(request.POST.get('resistance', 0))
            power = intensity * resistance  # Power calculation formula
        except ValueError:
            power = 'Invalid input. Please enter valid numbers.'

    return render(request, 'serverapp/power_calculator.html', {
        'intensity': intensity,
        'resistance': resistance,
        'power': power,
    })


