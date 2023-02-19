from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Make module in app'

    def add_arguments(self, parser):
        parser.add_argument('app_dir', type=str)
        parser.add_argument('module_name', type=str)

    def handle(self, *args, **kwargs):
        self.stdout.write("You gonna make module at %s" % kwargs['app_dir'])
        self.stdout.write("With %s as the module's name" % kwargs['module_name'])
