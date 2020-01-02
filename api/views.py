from whiskydatabase.models import WhiskyInfo, Distillery
from rest_framework import viewsets
from api.serializers import WhiskySerializer, DistillerySerializer
import re


class WhiskyViewSet(viewsets.ModelViewSet):
    queryset = WhiskyInfo.objects.all()
    serializer_class = WhiskySerializer
    

class DistilleryViewSet(viewsets.ModelViewSet):
    queryset = Distillery.objects.all()
    serializer_class = DistillerySerializer

""" class MorePostViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = MorePostSerializer

    def get_queryset(self):
        target_name = self.request.query_params.get('target')
        num = int(self.request.query_params.get('num'))
        target_dict = {'author-share': '名家分享', 'rookie': '新手村'}
        category_list = []
        status_tuple = post_status(self.request)

        if target_name == "hot-ranking":
            queryset = Post.objects.filter(status__in=status_tuple, category__is_active=True).distinct().order_by('-created_on')[num:num+10]
        elif target_name in target_dict:
            parent_cat = Menu.objects.get(title=target_dict[target_name])
            submenus = Menu.objects.filter(parent=parent_cat)
            for i in submenus:
                cat = Category.objects.get(name=i.title)
                category_list.append(cat)
            queryset = Post.objects.filter(status__in=status_tuple, category__is_active=True, category__in=category_list).distinct().order_by('-created_on')[num:num+9]
        else:
            category = Category.objects.get(name=target_name)
            queryset = Post.objects.filter(status__in=status_tuple, category__is_active=True, category__in=[category]).distinct().order_by('-created_on')[num:num+10]

        return queryset """