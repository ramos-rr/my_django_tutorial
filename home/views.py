from django.views import generic


class HomeView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'menu_list'

    def get_queryset(self):
        return ['admin', 'polls']
