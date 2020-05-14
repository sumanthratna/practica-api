import django
from wsgiref.simple_server import make_server
from django.core.handlers.wsgi import WSGIHandler
import cProfile

pr = cProfile.Profile()
pr.enable()
django.setup()
httpd = make_server('localhost', 8000, WSGIHandler())
# httpd.serve_forever()
# httpd.shutdown()
# httpd.close()
# httpd.server_close()
pr.disable()
pr.print_stats(sort='time')
pr.dump_stats('practica_api.profile')
