from rest_framework.permissions import BasePermission

class IsAuthenticatedOrReadOnly(BasePermission):  #  Не работает

    def has_object_permission(self, request, view, obj):
        who = request.user
        what = obj.creator  # user => в бд записан как creator
        if request.user.is_superuser and request.user.is_staff:
            return True
        elif who == what:
            return True