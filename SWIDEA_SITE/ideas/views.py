from django.shortcuts import render, redirect
from .models import Idea, IdeaStar, DevTool
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.
def idea_list(request):
    sort = request.GET.get('sort', 'id') 
    
    if sort == 'interest':
        ideas_list = Idea.objects.all().order_by('-interest', 'id') 
    elif sort == 'title':
        ideas_list = Idea.objects.all().order_by('title') 
    else:
        ideas_list = Idea.objects.all().order_by('id') 

    paginator = Paginator(ideas_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'idea_list.html', {
        'ideas': page_obj,
        'sort': sort 
    })

def idea_create(request):
    if request.method == "POST":
        devtool_id = request.POST.get('devtool')
        devtool_obj = DevTool.objects.get(id=devtool_id)
        
        Idea.objects.create(
            title=request.POST["title"],
            image=request.FILES.get("image"),
            content=request.POST["content"],
            interest=request.POST["interest"],
            devtool=devtool_obj,
        )
        return redirect("ideas:idea_list")
    
    devtools = DevTool.objects.all()
    return render(request, "idea_create.html", {"devtools": devtools})

def idea_detail(request, pk):
    idea = get_object_or_404(Idea, id=pk)
    context = {
        "idea" : idea
    }
    return render(request, "idea_detail.html", context)

def idea_update(request, pk):
    idea = Idea.objects.get(id = pk)
    if request.method == "POST":
        idea.title = request.POST["title"]
        new_image = request.FILES.get("image")
        if new_image:
            idea.image = new_image
        idea.content = request.POST["content"]
        idea.interest = request.POST["interest"]
        devtool_id = request.POST.get('devtool')
        if devtool_id:
            idea.devtool = DevTool.objects.get(id=devtool_id)
            
        idea.save() 
        return redirect("ideas:idea_detail", pk)
    devtools = DevTool.objects.all()
    context = { 
        "idea" : idea,
        "devtools": devtools 
    }
    return render(request, "idea_update.html", context)

def idea_delete(request, pk):
    if request.method == "POST":
        idea = Idea.objects.get(id=pk)
        idea.delete()
    return redirect("ideas:idea_list")

def devtool_list(request):
    devtools = DevTool.objects.all()
    context = { "devtools" : devtools } 
    return render(request, 'devtool_list.html', context)

def devtool_create(request):
    if request.method == "POST":
        DevTool.objects.create(
            name = request.POST["name"],
            kind = request.POST["kind"],
            description = request.POST["description"],
        )
        return redirect("ideas:devtool_list")
    return render(request, "devtool_create.html")

def devtool_detail(request, pk):
    devtool = get_object_or_404(DevTool, id=pk)
    ideas = devtool.idea_set.all() 
    context = {
        "devtool" : devtool
    }
    return render(request, 'devtool_detail.html', context)

def devtool_update(request, pk):
    devtool = DevTool.objects.get(id = pk)
    if request.method == "POST":
        devtool.name = request.POST["name"]
        devtool.kind = request.POST["kind"]
        devtool.description = request.POST["description"]
        devtool.save()
        return redirect("ideas:devtool_detail", pk)
    context = { "devtool" : devtool }
    return render(request, "devtool_update.html", context)

def devtool_delete(request, pk):
    if request.method == "POST":
        devtool = DevTool.objects.get(id=pk)
        devtool.delete()
    return redirect("ideas:devtool_list")


def idea_star(request, pk):
    idea = Idea.objects.get(pk=pk)
    star, created = IdeaStar.objects.get_or_create(idea=idea)

    star.is_starred = not star.is_starred
    star.save()

    return JsonResponse({
        'is_starred': star.is_starred
    })

def adjust_interest(request, pk):
    idea = Idea.objects.get(pk=pk)
    action = request.GET.get('action')
    
    if action == 'plus':
        idea.interest += 1
    elif action == 'minus' and idea.interest > 0:
        idea.interest -= 1
        
    idea.save()
    return JsonResponse({'new_interest': idea.interest})