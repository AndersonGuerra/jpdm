from django.http import HttpResponse
from django.shortcuts import render
from .forms import DinoForm, AlimentacaoForm, EspecieForm, GeneroForm, SubordemForm, OrdemForm
from .models import Dinossauro, Alimentacao, Especie, Genero, Subordem, Ordem
# nao sei o motivo de ter importado de PIL
from PIL import Image

def inicio(request):
    return render(request, 'inicio.html')

def cadastro(request):
    if request.method == 'POST':
        if 'cadastro' in request.POST:
            if request.POST['cadastro'] == 'Cadastrar Dinossauro':
                formulario = DinoForm()
            elif request.POST['cadastro'] == 'Cadastrar Alimentação':
                formulario = AlimentacaoForm()
            elif request.POST['cadastro'] == 'Cadastrar Espécie':
                formulario = EspecieForm()
            elif request.POST['cadastro'] == 'Cadastrar Gênero':
                formulario = GeneroForm()
            elif request.POST['cadastro'] == 'Cadastrar Subordem':
                formulario = SubordemForm()
            elif request.POST['cadastro'] == 'Cadastrar Ordem':
                formulario = OrdemForm()

            return render(request, 'cadastro.html', {'formulario': formulario})

        if 'dinossauro' in request.POST:
            formulario_feito = DinoForm(request.POST, request.FILES)
        elif 'alimentação' in request.POST:
            formulario_feito = AlimentacaoForm(request.POST)
        elif 'espécie' in request.POST:
            formulario_feito = EspecieForm(request.POST)
        elif 'gênero' in request.POST:
            formulario_feito = GeneroForm(request.POST)
        elif 'subordem' in request.POST:
            formulario_feito = SubordemForm(request.POST)
        elif 'ordem' in request.POST:
            formulario_feito = OrdemForm(request.POST)
        if formulario_feito.is_valid():
            formulario_feito.save()
            return render(request, 'cadastro.html',{'cadastrado': True})

    else:
        return render(request, 'cadastro.html')

def gerenciar(request):
    if 'gerenciar' in request.GET:
        gerenciar_tipo = request.GET['gerenciar']
        dados = {'dado': 'Não existem itens cadastrados.', 'tipo': 'vazio'}
        if gerenciar_tipo == 'Gerenciar Dinossauro':
            dino = Dinossauro.objects.all()
            if dino.exists():
                dados['dado'] = dino
                dados['tipo'] = 'dino'
        elif gerenciar_tipo == 'Gerenciar Alimentação':
            alimentacao = Alimentacao.objects.all()
            if alimentacao.exists():
                dados['dado'] = alimentacao
                dados['tipo'] = 'alimentacao'
        elif gerenciar_tipo == 'Gerenciar Espécie':
            especie = Especie.objects.all()
            if especie.exists():
                dados['dado'] = especie
                dados['tipo'] = 'especie'
        elif gerenciar_tipo == 'Gerenciar Gênero':
            genero = Genero.objects.all()
            if genero.exists():
                dados['dado'] = genero
                dados['tipo'] = 'genero'
        elif gerenciar_tipo == 'Gerenciar Subordem':
            subordem = Subordem.objects.all()
            if subordem.exists():
                dados['dado'] = subordem
                dados['tipo'] = 'subordem'
        elif gerenciar_tipo == 'Gerenciar Ordem':
            ordem = Ordem.objects.all()
            if ordem.exists():
                dados['dado'] = ordem
                dados['tipo'] = 'ordem'

        return render(request, 'gerenciar.html', dados)

    else:
        return HttpResponse('Ação não permitida')

def alterar(request):
    if 'alterado' in request.POST:
        if 'altera_dino' in request.POST:
            dino = Dinossauro.objects.get(id=request.POST['altera_dino'])
            formulario = DinoForm(request.POST, request.FILES, instance=dino)

        elif 'altera_alimento' in request.POST:
            alimento = Alimentacao.objects.get(id=request.POST['altera_alimento'])
            formulario = AlimentacaoForm(request.POST, request.FILES, instance=alimento)

        elif 'altera_especie' in request.POST:
            especie = Especie.objects.get(id=request.POST['altera_especie'])
            formulario = EspecieForm(request.POST, request.FILES, instance=especie)

        elif 'altera_genero' in request.POST:
            genero = Genero.objects.get(id=request.POST['altera_genero'])
            formulario = GeneroForm(request.POST, request.FILES, instance=genero)

        elif 'altera_subordem' in request.POST:
            subordem = Subordem.objects.get(id=request.POST['altera_subordem'])
            formulario = SubordemForm(request.POST, request.FILES, instance=subordem)

        elif 'altera_ordem' in request.POST:
            ordem = Ordem.objects.get(id=request.POST['altera_ordem'])
            formulario = OrdemForm(request.POST, request.FILES, instance=ordem)
        try:
            formulario.save()
            msg = 'Item alterado com sucesso.'
        except:
            msg = 'Falha ao alterar item.'

        return render(request, 'alterar.html', {'msg': msg})
    else:
        if 'dino_alterar' in request.POST:
            dinossauro = Dinossauro.objects.get(id=request.POST['dino_id'])
            id_item = dinossauro.id
            tipo = 'dinossauro'
            formulario = DinoForm(instance=dinossauro)
        elif 'alimento_alterar' in request.POST:
            alimento = Alimentacao.objects.get(id=request.POST['alimento_id'])
            id_item = alimento.id
            tipo = 'alimentação'
            formulario = AlimentacaoForm(instance=alimento)
        elif 'especie_alterar' in request.POST:
            especie = Especie.objects.get(id=request.POST['especie_id'])
            id_item = especie.id
            tipo = 'espécie'
            formulario = EspecieForm(instance=especie)
        elif 'genero_alterar' in request.POST:
            genero = Genero.objects.get(id=request.POST['genero_id'])
            id_item = genero.id
            tipo = 'gênero'
            formulario = GeneroForm(instance=genero)
        elif 'subordem_alterar' in request.POST:
            subordem = Subordem.objects.get(id=request.POST['subordem_id'])
            id_item = subordem.id
            tipo = 'subordem'
            formulario = SubordemForm(instance=subordem)
        elif 'ordem_alterar' in request.POST:
            ordem = Ordem.objects.get(id=request.POST['ordem_id'])
            id_item = ordem.id
            tipo = 'ordem'
            formulario = OrdemForm(instance=ordem)

        try:
            return render(request, 'alterar.html', {'formulario': formulario, 'id': id_item, 'tipo':tipo})
        except:
            return HttpResponse('caminho inválido')

def excluir(request):
    if 'confirma_exclusao' in request.POST:
        #if 'dino_id' or 'alimento_id' in request.POST:
        #    print(request.POST)
        if 'dino_id' in request.POST:
            modelo = Dinossauro.objects.get(id=request.POST['dino_id'])
        elif 'alimento_id' in request.POST:
            modelo = Alimentacao.objects.get(id=request.POST['alimento_id'])
        elif 'especie_id' in request.POST:
            modelo = Especie.objects.get(id=request.POST['especie_id'])
        elif 'genero_id' in request.POST:
            modelo = Genero.objects.get(id=request.POST['genero_id'])
        elif 'subordem_id' in request.POST:
            modelo = Subordem.objects.get(id=request.POST['subordem_id'])
        elif 'ordem_id' in request.POST:
            modelo = Ordem.objects.get(id=request.POST['ordem_id'])
        try:
            modelo.delete()
            return render(request, 'excluir.html', {'exclusao_ok': True})
        except:
            return render(request, 'excluir.html', {'exclusao_fail': 'nao excluido'})

    else:
        if 'dino_excluir' in request.POST:
            dados_exclusao = Dinossauro.objects.get(id=request.POST['dino_id'])
            tipo = 'dinossauro'
        elif 'alimento_excluir' in request.POST:
            dados_exclusao = Alimentacao.objects.get(id=request.POST['alimento_id'])
            tipo = 'alimentação'
        elif 'especie_excluir' in request.POST:
            dados_exclusao = Especie.objects.get(id=request.POST['especie_id'])
            tipo = 'espécie'
        elif 'genero_excluir' in request.POST:
            dados_exclusao = Genero.objects.get(id=request.POST['genero_id'])
            tipo = 'gênero'
        elif 'subordem_excluir' in request.POST:
            dados_exclusao = Subordem.objects.get(id=request.POST['subordem_id'])
            tipo = 'subordem'
        elif 'ordem_excluir' in request.POST:
            dados_exclusao = Ordem.objects.get(id=request.POST['ordem_id'])
            tipo = 'ordem'
        try:
            return render(request, 'excluir.html', {'dados': dados_exclusao, 'tipo': tipo})
        except:
            return render(request, 'excluir.html', {'msg': 'Dados nao existentes'})

def sobre(request):
    if 'dino_sobre' in request.POST:
        dados = Dinossauro.objects.get(id=request.POST['dino_id'])
        tipo = 'dinossauro'
    elif 'alimento_sobre' in request.POST:
        dados = Alimentacao.objects.get(id=request.POST['alimento_id'])
        tipo = 'alimentação'
    elif 'especie_sobre' in request.POST:
        dados = Especie.objects.get(id=request.POST['especie_id'])
        tipo = 'espécie'
    elif 'genero_sobre' in request.POST:
        dados = Genero.objects.get(id=request.POST['genero_id'])
        tipo = 'gênero'
    elif 'subordem_sobre' in request.POST:
        dados = Subordem.objects.get(id=request.POST['subordem_id'])
        tipo = 'subordem'
    elif 'ordem_sobre' in request.POST:
        dados = Ordem.objects.get(id=request.POST['ordem_id'])
        tipo = 'ordem'
    try:
        return render(request, 'sobre.html', {'dados': dados, 'tipo': tipo})
    except:
        return render(request, 'sobre.html', {'erro': True})