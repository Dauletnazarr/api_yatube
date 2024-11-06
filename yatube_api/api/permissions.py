from rest_framework.permissions import BasePermission


class IsAuthorOrReadOnly(BasePermission):
    """
    Разрешение, позволяющее редактировать объект только автору.
    Остальным пользователям доступен только просмотр.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешаем безопасные методы (GET, HEAD, OPTIONS) для всех
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        # Для остальных методов проверяем, является ли пользователь автором
        return obj.author == request.user
