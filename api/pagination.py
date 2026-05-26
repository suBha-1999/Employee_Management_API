from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page-size'
    page_query_param = 'page-num'
    max_page_size = 10

    def get_paginated_response(self, data):
        # return Response({
        #     'next' : self.get_next_link(),
        #     'previous' : self.get_previous_link(),
        #     'count' : self.page.paginator.count(),
        #     'page-size' : self.page_size,
        #     'request' : data,
        # })

        return Response({
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'page_size': self.get_page_size(self.request),
            'current_page': self.page.number,
            'total_pages': self.page.paginator.num_pages,
            'results': data
        })
    


class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    limit_query_param = 'limit'
    offset_query_param = 'offset'
    max_limit = 10

    def get_paginated_response(self, data):
        return Response({
            'count': self.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'limit': self.limit,
            'offset': self.offset,
            'results': data
        })