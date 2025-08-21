from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import UserFavouriteArticle, Article
from django.db import IntegrityError

# Create your tests here.

class UserAuthenticationTest(TestCase):

    def test_FavouritesView_accesible_for_authenticated_users(self):
        User.objects.create_user(username="testuser", password="password2025")
        self.client.login(username="testuser", password="password2025")
        response = self.client.get(reverse("favourites"))
        self.assertContains(response, "testuser")

    def test_FavouritesView_accesible_for_anonymous_users(self):
        response = self.client.get(reverse("favourites"))
        self.assertRedirects(response, expected_url=f"{reverse('login')}?next={reverse('favourites')}")


    def test_PublicationsView_accesible_for_authenticated_users(self):
        User.objects.create_user(username="testuser", password="password2025")
        self.client.login(username="testuser", password="password2025")
        

    def test_PublicationsView_accesible_for_anonymous_users(self):
        response = self.client.get(reverse("publications"))
        self.assertRedirects(response, expected_url=f"{reverse('login')}?next={reverse('publications')}")


    def test_PublishView_accesible_for_authenticated_users(self):
        User.objects.create_user(username="testuser", password="password2025")
        self.client.login(username="testuser", password="password2025")
        response = self.client.get(reverse("publish"))
        self.assertContains(response, "testuser")

    def test_PublishView_accesible_for_anonymous_users(self):
        response = self.client.get(reverse("publish"))
        self.assertRedirects(response, expected_url=f"{reverse('login')}?next={reverse('publish')}")


    def test_UserCreationForm_accesible_for_authenticated_users(self):
        User.objects.create_user(username="testuser", password="password2025")
        self.client.login(username="testuser", password="password2025")
        response = self.client.get(reverse("register"), follow=True)
        self.assertRedirects(response, expected_url=reverse("articles"))

    def test_UserCreationForm_accesible_for_anonymous_users(self):
        response = self.client.get(reverse("register"), follow=True)
        self.assertEqual(response.status_code, 200)

    
class ArticleModelTest(TestCase):
    
    def test_same_data_on_db(self):

        user1 = User.objects.create_user(username="user1", password="password!2025")
        article1 = Article.objects.create(title="title", author=user1, synopsis="synopsis", content="content")
        
        fav1 = UserFavouriteArticle(user=user1, article=article1)
        fav1.save()
        with self.assertRaises(IntegrityError):
            fav2 = UserFavouriteArticle(user=user1, article=article1)
            fav2.save()