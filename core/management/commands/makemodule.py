from django.core.management.base import BaseCommand
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Make module in app'

    # def add_arguments(self, parser):
    #     # parser.add_argument('app_dir', type=str)
    #     # parser.add_argument('module_name', type=str)

    def handle(self, *args, **kwargs):
        app_name = input("App name: ")
        model_name = input("Model name: ")

        if self.is_app_exist(app_name) != True:
            self.stdout.write("App directory doesn't exist")
            self.stdout.write(
                "Check if you miss type it or create the app first")
            return False

        self.stdout.write("You gonna make module at %s" % app_name)
        self.stdout.write("With module name %s" % model_name.capitalize())

        app_dir = os.path.join(settings.BASE_DIR, app_name)
        model_name = model_name.capitalize()

        self.write_model(app_dir, model_name)
        self.update_init_model(app_dir, model_name)
        self.write_serializer(app_dir, app_name, model_name)
        self.write_view(app_dir, app_name, model_name)
        self.update_app_urls(app_dir, app_name, model_name)

    # Writing and updating file

    def write_model(self, app_dir, model_name):
        try:
            model_file = open(f"{app_dir}/models/{model_name}.py", "a")
            model_file.write(f'''from django.db import models
import uuid


class {model_name}(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Your field here
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']
''')
            model_file.close()

            self.stdout.write("Success making model %s" % model_name)

        except:
            self.stdout.write(
                "There's something wrong while making model %s" % model_name)
            return False

    def update_init_model(self, app_dir, model_name):
        try:
            model_init_file = open(f"{app_dir}/models/__init__.py", 'a')
            model_init_file.write(f"from .{model_name} import {model_name}")
            
            
            self.stdout.write("Success updating %s urls" % app_dir)
        except:
            self.stdout.write(
                "There's something wrong while making model %s" % model_name)
            return False
            

    def write_serializer(self, app_dir, app_name, model_name):
        try:
            serializer_file = open(
                f"{app_dir}/serializers/{model_name}Serializer.py", "a")
            serializer_file.write(f'''from rest_framework import serializers
from {app_name}.models import {model_name}


class {model_name}Serializer(serializers.ModelSerializer):
    class Meta:
        model = {model_name}
        fields = ['id', 'created_at', 'updated_at']
''')
            serializer_file.close()

            self.stdout.write("Success making serializer %s" % model_name)

        except:
            self.stdout.write(
                "There's something wrong while making serializer %s" % model_name)
            return False

    def write_view(self, app_dir, app_name, model_name):
        try:
            view_file = open(f"{app_dir}/views/{model_name}ViewSet.py", "a")
            view_file.write(f'''from {app_name}.models import {model_name}
from rest_framework import viewsets
from {app_name}.serializers.{model_name}Serializer import {model_name}Serializer


class {model_name}ViewSet(viewsets.ModelViewSet):
    """
    {app_name.upper()} endpoint that allows {model_name} to be viewed or edited.
    """
    queryset = {model_name}.objects.all().order_by('-created_at')
    serializer_class = {model_name}Serializer
''')
            view_file.close()
            self.stdout.write("Success making view %s" % model_name)

        except:
            self.stdout.write(
                "There's something wrong while making serializer %s" % model_name)
            return False

    def update_app_urls(self, app_dir, app_name, model_name):
        try:
            with open(f"{app_dir}/urls.py", 'r+') as urls_file:
                lines = urls_file.readlines()
                
                # Import viewsets to route
                import_new_route_line = lines.index("# Register new viewSet above\n")
                lines.insert(import_new_route_line, f'from {app_name}.views import {model_name}ViewSet\n')

                # Register viewsets to route
                register_new_route_line = lines.index("# Register new view above\n")
                lines.insert(register_new_route_line, f'router.register(r\'{model_name.lower()}s\', UserViewSet.UserViewSet, basename=\'{model_name}s\')\n')
                
                urls_file.seek(0)
                
                urls_file.writelines(lines)
                
                urls_file.close()
            
            self.stdout.write("Success updating %s urls" % app_dir)
        except:
            self.stdout.write(
                    "There's something wrong while updating urls %s" % model_name)
            return False

    # Utils
    def is_app_exist(self, app_dir):
        return os.path.exists(os.path.join(settings.BASE_DIR, app_dir))
