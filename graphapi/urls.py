from django.urls import path
from django.contrib.auth.decorators import login_required
from graphene_django.views import GraphQLView 
from .schemas import schema


class CustomGraphQLView(GraphQLView):
    def execute_graphql_request(self, request,
        data, query, variables, operation_name, 
        show_graphiql = False):
        return super().execute_graphql_request(
            request, data, query, variables, operation_name, show_graphiql
        )
        
@login_required(login_url = 'admin')
def graphql_view(request):
    view = CustomGraphQLView.as_view(graphiql = True, schema = schema) # при регистрации становится . связано с разрешениями. Если пользователю не дали разрешение, в атком случае True.
    return view(request) # разрешено или нет опрделяется в запросе

urlpatterns = (
    path('', graphql_view),
    
)






