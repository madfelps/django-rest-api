from django.http import JsonResponse

def alunos(request):
    if request.method == 'GET':
        aluno = {'id': 1, 'nome': 'Felipe'}
        return JsonResponse(aluno)

# Create your views here.
