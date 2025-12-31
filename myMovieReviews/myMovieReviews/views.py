from django.shortcuts import render, redirect
from .models import Review

# Create your views here.
def movie_list(request):
    sort = request.GET.get('sort', '-id') 
    reviews = Review.objects.all().order_by(sort)
    context = {
         "reviews" : reviews,
         "sort" : sort,
    }
    return render(request, "movie_list.html", context)

def movie_detail(request, pk):
    review = Review.objects.get(id=pk)
    runtime_hour = review.RT // 60
    runtime_min = review.RT % 60
    context = {
        "review": review,
        "runtime_hour": runtime_hour,
        "runtime_min": runtime_min,
    }
    return render(request, "movie_detail.html", context)

def movie_create(request):
    if request.method == "POST" :
        Review.objects.create(
            title = request.POST["title"],
            poster = request.POST["poster"],
            year = request.POST["year"],
            genre = request.POST["genre"],
            rate = request.POST["rate"],
            RT = request.POST["RT"],
            content = request.POST["content"],
            Dir = request.POST["Dir"],
            MC = request.POST["MC"]
        )
        return redirect("myMovieReviews:list")
    return render(request, "movie_create.html")

def movie_update(request, pk):
    review = Review.objects.get(id=pk)
    if request.method == "POST":
            review.title = request.POST["title"]
            review.poster = request.POST["poster"]
            review.year = request.POST["year"]
            review.genre = request.POST["genre"]
            review.rate = request.POST["rate"]
            review.RT = request.POST["RT"]
            review.content = request.POST["content"]
            review.Dir = request.POST["Dir"]
            review.MC = request.POST["MC"]
            review.save()
            return redirect("myMovieReviews:detail", pk)
    context = {"review" : review}
    return render(request, "movie_update.html", context)

def movie_delete(request, pk):
    if request.method == "POST":
        review = Review.objects.get(id=pk) 
        review.delete() 
    return redirect("myMovieReviews:list")