from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination
)

class EssayLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10,

class EssayPageNumberPagination(PageNumberPagination):
    page_size = 2
