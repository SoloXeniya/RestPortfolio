from rest_framework.pagination import PageNumberPagination

class ContactPagination(PageNumberPagination):
    #колличество объектов на тсранице
    page_size = 100
    
    #параметр запроса для указания колличества объектов на странице
    page_size_query_param = 'page_size'
    
    #макс. размер страницы, который клиент может указать в запросе
    max_page_size = 100
    
    #параметр запроса для указания номера страницы
    page_query_param = 'p'
    
    #строки, которые могут использовать для обозначения поледней страницы
    last_page_strings = ['end']
    
    