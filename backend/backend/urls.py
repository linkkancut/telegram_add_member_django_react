from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todo import views as todoViews
from user import views as userViews
from group import views as groupViews
from member import views as memberViews
from group_member import views as groupMemberViews


router = routers.DefaultRouter()
router.register(r'todos', todoViews.TodoView, 'todo')
router.register(r'users', userViews.UserView, 'user')
router.register(r'group', groupViews.GroupView, 'group')
router.register(r'member', memberViews.MemberView, 'member')
router.register(r'group-member',
                groupMemberViews.GroupMemberView, 'group-member')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
