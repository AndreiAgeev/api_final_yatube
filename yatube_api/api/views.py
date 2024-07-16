from django.shortcuts import get_object_or_404
from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import (GenericViewSet,
                                     ModelViewSet,
                                     ReadOnlyModelViewSet)

from . import excpetions, serializers
from .permissions import AuthorOrReadOnly
from posts.models import Follow, Group, Post, User


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = (AllowAny,)


class CommentViewSet(ModelViewSet):
    permission_classes = (AuthorOrReadOnly,)
    serializer_class = serializers.CommentSerializer

    def get_post_object(self):
        post_id = self.kwargs.get('post_id')
        return get_object_or_404(Post, pk=post_id)

    def get_queryset(self):
        post = self.get_post_object()
        return post.comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.get_post_object()
        )


class FollowViewSet(CreateModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = serializers.FollowSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def perform_checks(self, user, follow_user):
        if follow_user == user:
            raise excpetions.FollowMyselfError
        if Follow.objects.filter(user=user, following=follow_user):
            raise excpetions.FollowTwiceError

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        follow_username = serializer.validated_data.get('following')
        follow_user = get_object_or_404(User, username=follow_username)
        self.perform_checks(user, follow_user)
        serializer.save(
            user=user,
            following=follow_user
        )
