from django.template import Context
from django.template.defaultfilters import slugify
from django.template.loader import get_template

from generate_scaffold.generators.base import BaseGenerator
from generate_scaffold.utils.directories import get_templates_in_dir


class AdminGenerator(BaseGenerator):

    # FIXME - Accomodate for empty urls.py, without 
    #         url imports.
    def render_admin(self, model):

        admin_module = self.get_app_module('admin')

        is_admin_available = \
            hasattr(admin_module, 'admin')

        class_name = model._meta.concrete_model.__name__

        urls_template = get_template('generate_scaffold/admin/admin.txt')
        c = {
            'is_admin_available': is_admin_available,
            'model_name': class_name,
        }
        return urls_template.render(Context(c))
