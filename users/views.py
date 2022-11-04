from django.shortcuts import render
import json
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from avito import settings
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from users.models import User, Location
from django.core.paginator import Paginator


class UserListView(ListView):
    model = User
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        super().get(self, *args, **kwargs)
        self.object_list = self.object_list.order_by("username")
        paginator = Paginator(object_list=self.object_list, per_page=settings.TOTAL_ON_PAGE)
        page = request.GET.get('page')
        page_obj = paginator.get_page(page)
        result = []
        for user in page_obj:
            result.append({"id": user.id,
                           "username": user.username,
                           "first_name": user.first_name,
                           "last_name": user.last_name,
                           "role": user.role,
                           "age": user.age,
                           "ads_count": user.ads.count()
                           })
        return JsonResponse({'ads': result, 'page': page_obj.number, 'total': page_obj.paginator.count}, safe=False,
                            json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class UserCreateView(CreateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'role', 'age', 'locations']

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        user = User.objects.create(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            role=data['role'],
            age=data['age'],
            password=data['password']
        )
        for loc in data['locations']:
            location, _ = Location.objects.get_or_create(name=loc)
            user.location.add(location)

        return JsonResponse(
            {'id': user.id,
             'username': user.username,
             'first_name': user.first_name,
             'last_name': user.last_name,
             'role': user.role,
             'age': age.role,
             'locations': [str(u) for u in user.location.all()]
             })


@method_decorator(csrf_exempt, name='dispatch')
class UserUpdateView(UpdateView):
    model = User
    fields = ['username', 'password', 'first_name', 'last_name', 'role', 'age', 'locations']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        data = json.loads(request.body)
        self.object.name = data['username']
        self.object.save()
        return JsonResponse({"id": self.object.id, "username": self.object.name}, safe=False,
                            json_dumps_params={'ensure_ascii': False})


@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({}, status=204)
