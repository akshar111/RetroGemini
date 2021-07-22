from django.shortcuts import render
from django.http import HttpResponse
from .models import Board, Status, Task

# Create your views here.

def board_view(request):
    all_status = Status.objects.all()
    all_task = Task.objects.all()
    all_board = Board.objects.all()
   
    if request.method == 'POST':
            if request.POST.get('name'):
                post=Task()
                post.name= request.POST.get('name')
                post.board=  'DEMO'
                post.status= all_status[0].name
                post.save()
                
                return render(request, 'board/board.html')  

    
    else:
        context = {
            'task':all_task,
        }
    
    return render(request, 'board/board.html', context)




