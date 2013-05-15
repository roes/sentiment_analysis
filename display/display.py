import logging
import os
import sqlite3

from pyramid.config import Configurator
from pyramid.events import ApplicationCreated
from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.view import view_config

from wsgiref.simple_server import make_server

logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))

@view_config(route_name='index', renderer='index.mako')
def index_view(request):
  rs = request.db.execute("select distinct company from reputation")
  companies = [row[0] for row in rs.fetchall()]
  return {'companies': companies}

@view_config(route_name='graph', xhr=True, renderer='json')
def graph_view_ajax(request):
  company = request.matchdict['company']
  rs = request.db.execute("select day, value from reputation where company = ? order by day", (company,))
  reputation = []
  aggregated_reputation = 0
  for row in rs.fetchall():
    aggregated_reputation += row[1]
    reputation.append([row[0], aggregated_reputation])
  #reputation = [[row[0], row[1]] for row in rs.fetchall()]
  return {'reputation': reputation, 'company':company}

@subscriber(NewRequest)
def new_request_subscriber(event):
  request = event.request
  settings = request.registry.settings
  request.db = sqlite3.connect(settings['db'])
  request.add_finished_callback(close_db_connection)

def close_db_connection(request):
  request.db.close()

if __name__ == '__main__':
  # configuration settings
  settings = {}
  settings['reload_all'] = True
  settings['debug_all'] = True
  settings['mako.directories'] = os.path.join(here, 'templates')
  settings['db'] = os.path.join(here, 'db/reputation.db')
  # configuration setup
  config = Configurator(settings=settings)
  config.add_route('index', '/')
  config.add_route('graph', '/graph/{company}')
  config.add_static_view('static', os.path.join(here, 'static'))
  config.scan()
  # serve app
  app = config.make_wsgi_app()
  server = make_server('0.0.0.0', 8080, app)
  server.serve_forever()
