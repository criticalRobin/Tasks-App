from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from core.user.models import MyUser
from core.user.forms import UserForm, UserUpdateForm


# Create your views here.
class UserListView(ListView):
    model = MyUser
    template_name = "list.html"

    # @method_decorator(login_required(login_url=reverse_lazy("login:login_view")))
    # @method_decorator(csrf_exempt)
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(self, request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Users List"
        context["list_url"] = reverse_lazy("user:user_list")
        context["entity"] = "Users"
        return context


class UserCreateView(CreateView):
    model = MyUser
    form_class = UserForm
    template_name = "create.html"
    success_url = reverse_lazy("user:user_list")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        password = request.POST.get("password")
        password_confirm = request.POST.get("password_confirm")

        if password == password_confirm:
            if form.is_valid():
                # aqui aun no se ha guardado el objeto en la base de datos, es decir no existe
                # por eso creo una variable user y guardo dentro el formulario
                user = form.save(commit=False)
                # commit = False, es para que no se guarde en la base de datos
                # de esta forma puedo modificar el objeto antes de guardarlo
                try:
                    validate_password(user.password, user)
                except ValidationError as e:
                    form.add_error("password", e)
                    return render(request, self.template_name, context={"form": form})
                user.password = make_password(password)
                if user.first_name[0] is not user.first_name[0].upper():
                    user.first_name = user.first_name.capitalize()
                if user.last_name[0] is not user.last_name[0].upper():
                    user.last_name = user.last_name.capitalize()
                user.save()
                return HttpResponseRedirect(self.success_url)
        else:
            form.add_error("password_confirm", "Passwords do not match")
        self.object = None
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(request, self.template_name, context)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Create User"
        context["list_url"] = reverse_lazy("user:user_list")
        context["entity"] = "Users"
        return context


class UserUpdateView(UpdateView):
    model = MyUser
    form_class = UserUpdateForm
    template_name = "create.html"
    success_url = reverse_lazy("user:user_list")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.form = self.get_form()

        if self.form.is_valid():
            self.object.first_name = self.form.cleaned_data["first_name"].capitalize()
            self.object.last_name = self.form.cleaned_data["last_name"].capitalize()
            self.object.save()
            return HttpResponseRedirect(self.success_url)
        return render(request, self.template_name, context={"form": self.form})

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Update User"
        context["list_url"] = reverse_lazy("user:user_list")
        context["entity"] = "Users"
        return context


class UserDeleteView(DeleteView):
    model = MyUser
    template_name = "delete.html"
    success_url = reverse_lazy("user:user_list")

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete User"
        context["list_url"] = reverse_lazy("user:user_list")
        context["entity"] = "Users"
        return context
