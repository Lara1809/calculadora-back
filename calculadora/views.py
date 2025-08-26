from django.shortcuts import render

# Create your views here.

def salario(request):
    if request.method == 'POST':
        salario = float(request.POST.get('salario', 0))
        extra = float(request.POST.get('extra', 0))

        total_salario = salario + extra

        resultado = {
            'salario': total_salario
        }

def calculo_casa(request):
    resultado = None

    if request.method == 'POST':
        aluguel = float(request.POST.get('aluguel', 0))
        agua = float(request.POST.get('agua', 0))
        luz = float(request.POST.get('luz', 0))
        gas = float(request.POST.get('gas', 0))

        total_gasto_casa = aluguel + agua + luz + gas

        resultado = {
            'gastos': total_gasto_casa
        }

def calculo_alimentacao(request):
    resultado = None

    if request.method == 'POST':
        mercado = float(request.POST.get('mercado', 0))
        fora = float(request.POST.get('fora', 0))
        horti_fruti = float(request.POST.get('horti_fruti', 0))
        feira = float(request.POST.get('feira', 0))
        outros = float(request.POST.get('outros', 0))

        total_gasto_alimentacao = mercado + fora + horti_fruti + feira + outros

        resultado = {
            'gastos': total_gasto_alimentacao
        }

def calculo_saude_beleza(request):
    resultado = None

    if request.method == 'POST':
        remedios = float(request.POST.get('remedios', 0))
        plano_saude = float(request.POST.get('plano_saude', 0))
        exames = float(request.POST.get('exames', 0))
        produtos_higiene = float(request.POST.get('produtos_higiene', 0))
        academia = float(request.POST.get('academia', 0))
        salao_beleza = float(request.POST.get('salao_beleza', 0))
        outros = float(request.POST.get('outros', 0))

        total_gasto_saude_beleza = remedios + plano_saude + exames + produtos_higiene + academia + salao_beleza + outros

        resultado = {
            'gastos': total_gasto_saude_beleza
        }

def calculo_transposte(request):
    resultado = None

    if request.method == 'POST':
        publico = float(request.POST.get('publico', 0))
        gasolina = float(request.POST.get('gasolina', 0))
        manutencao_veiculo = float(request.POST.get('manutencao_veiculo', 0))
        seguro = float(request.POST.get('seguro', 0))
        taxi = float(request.POST.get('taxi', 0))
        outros = float(request.POST.get('outros', 0))

        total_gasto_transposte = publico + gasolina + manutencao_veiculo + seguro + taxi + outros

        resultado = {
            'gastos': total_gasto_transposte
        }

def calculo_educacao(request):
    resultado = None

    if request.method == 'POST':
        mensalidade = float(request.POST.get('mensalidade', 0))
        material = float(request.POST.get('material', 0))
        cursos = float(request.POST.get('cursos', 0))
        outros = float(request.POST.get('outros', 0))

        total_gasto_educacao = mensalidade + material + cursos + outros

        resultado = {
            'gastos': total_gasto_educacao
        }

def calculo_extra(request):
    resultado = None

    if request.method == 'POST':
        viagens = float(request.POST.get('viagens', 0))
        roupas = float(request.POST.get('roupas', 0))
        cinema = float(request.POST.get('cinema', 0))
        shows = float(request.POST.get('shows', 0))
        festas = float(request.POST.get('festas', 0))
        presentes = float(request.POST.get('presentes', 0))
        animais = float(request.POST.get('animais', 0))
        outros = float(request.POST.get('outros', 0))

        total_gasto_extra = viagens + roupas + cinema + shows + festas + presentes + animais + outros

        resultado = {
            'gastos': total_gasto_extra
        }

def gastos_totais(request):
    resultado = None

    if request.method == 'POST':
        valor_total = total_gasto_casa + total_gasto_alimentacao + total_gasto_saude_beleza + total_gasto_transposte + total_gasto_educacao + total_gasto_extra 
        saldo_restante = salario - valor_total

        resultado = {
            'valor_total': valor_total,
            'saldo_restante': saldo_restante
        }
