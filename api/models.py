from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']

class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        authentication = CustomAuthentication()
        authorization = Authorization()

#    def hydrate(self, bundle):
#        bundle.obj.category_id = bundle.data['category_id']
#        return bundle

#    def dehydrate(self, bundle):
#        bundle.data['category_id'] = bundle.obj.category
#        return bundle