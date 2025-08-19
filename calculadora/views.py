from django.shortcuts import render

# Create your views here.

def salario(request):
    return render(request, 'salario.html')

def casa(request):
    return render(request, 'casa.html')

def alimentacao(request):
    return render(request, 'alimentacao.html')

def calculo_casa(request):
    resultado = None

    if request.method == 'POST':
        aluguel = float(request.POST.get('aluguel', 0))
        agua = float(request.POST.get('agua', 0))
        luz = float(request.POST.get('luz', 0))
        gas = float(request.POST.get('gas', 0))
        
        total_gastos = aluguel + agua + luz + gas

        resultado = {
            'gastos': total_gastos
        }

    return render(request, 'casa.html', {'resultado': resultado})
