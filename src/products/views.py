from django.contrib import messages
from django.db.models import Avg, Count
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CommentForm
from .models import Category, Comment, Product


def product_list(request: HttpRequest, category_slug: str | None = None) -> HttpResponse:
    """Render the product overview, optionally filtered by a category slug.

    :param request: The incoming HTTP request.
    :param category_slug: Optional category slug used to filter the product list.
    :return: The rendered ``products.html`` response with categories and products.
    """
    categories = Category.objects.all()
    products = Product.objects.select_related("category").annotate(
        avg_rating=Avg("comments__rating"), total_ratings=Count("comments")
    )
    if category_slug:
        products = products.filter(category__slug=category_slug)
    return render(request, "products.html", {"categories": categories, "products": products})


def product_detail(request: HttpRequest, category_slug: str, pk: int) -> HttpResponse:
    """Render a single product page and handle rating/comment submissions.

    :param request: The incoming HTTP request.
    :param category_slug: Slug of the category the product belongs to.
    :param pk: Primary key of the product to display.
    :return: The rendered ``product.html`` response, or a redirect after a successful POST.
    """
    product = get_object_or_404(
        Product.objects.select_related("category").annotate(
            avg_rating=Avg("comments__rating"), total_ratings=Count("comments")
        ),
        pk=pk,
        category__slug=category_slug,
    )

    related_products = (
        Product.objects.filter(category=product.category)
        .exclude(pk=product.pk)
        .annotate(avg_rating=Avg("comments__rating"), total_ratings=Count("comments"))
        .order_by("-avg_rating", "-total_ratings", "name")[:8]
    )

    comments = product.comments.select_related("user").order_by("-created_at")

    if request.method == "POST":
        form = CommentForm(request.POST, initial={"user": request.user if request.user.is_authenticated else None})
        if form.is_valid():
            rating = form.cleaned_data["rating"]
            text = form.cleaned_data.get("text", "")

            if request.user.is_authenticated:
                # Upsert: update existing comment or create a new one
                comment, created = Comment.objects.get_or_create(
                    product=product, user=request.user, defaults={"rating": rating, "text": text}
                )
                if not created:
                    comment.rating = rating
                    comment.text = text
                    comment.save()
                messages.success(request, "Your rating was {}.".format("submitted" if created else "updated"))
            else:
                # Guest: create a new comment (no uniqueness constraint)
                comment = form.save(commit=False)
                comment.product = product
                comment.save()
                messages.success(request, "Thank you for your rating.")
            # Flag setzen für "Formular nach Save leeren"
            request.session["clear_comment_form"] = True

            return redirect("product_detail", category_slug=category_slug, pk=product.pk)
    else:
        clear_form = request.session.pop("clear_comment_form", False)

        if clear_form:
            # 👉 Nach Speichern: alles leer
            form = CommentForm()

        else:
            # 👉 Normalfall: vorhandene Bewertung anzeigen
            initial = {}

            if request.user.is_authenticated:
                existing = product.comments.filter(user=request.user).first()

                if existing:
                    initial = {
                        "rating": existing.rating,
                        "text": existing.text,
                    }

            form = CommentForm(initial=initial)

    return render(
        request,
        "product.html",
        {"product": product, "comments": comments, "related_products": related_products, "form": form},
    )
