
from rest_framework_nested import routers

from . import views

# router = SimpleRouter()
# router = DefaultRouter()
# router.register('books', views.BookViewSet, basename='books')
# router.register('authors', views.AuthorViewSet, basename='authors')
# router.register('reviews', views.ReviewViewSet, basename='reviews')

router = routers.DefaultRouter()
router.register('books', views.BookViewSet)
router.register('authors', views.AuthorViewSet)
router.register('reviews', views.ReviewViewSet, basename='reviews')

books_router = routers.NestedDefaultRouter(router, 'books', lookup='book')
books_router.register('reviews', views.ReviewViewSet, basename='books-reviews')

urlpatterns = router.urls + books_router.urls

# urlpatterns = router.urls
# urlpatterns = [
#     path('', include(router.urls)),
#     path('', include(router.urls))
# ]

# urlpatterns = [
#     path('book/', views.book_list),
#     path('book/<int:pk>', views.book_detail),
#     path('author', views.author_list),
#     path('author<int:pk>', views.author_list, name="author-detail")
#     # path('welcome/', views.welcome),
#     # path('hello/', views.hello),
#     # path('books/pk/', views.get_books)
# ]
