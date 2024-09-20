from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from libs.connection import Connection

connectionInstance = Connection()

class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(
	('0.0.0.0', 8000),
	RequestHandler,
	logRequests=False,
	allow_none=True
) as server:
	server.register_introspection_functions()
	server.register_instance(connectionInstance)
	server.serve_forever()