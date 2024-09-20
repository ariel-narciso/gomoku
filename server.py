from xmlrpc.server import SimpleXMLRPCServer, SimpleXMLRPCRequestHandler
from gomoku import Gomoku
from connection import Connection

connectionInstance = Connection(Gomoku(5, 3))

class RequestHandler(SimpleXMLRPCRequestHandler):
	rpc_paths = ('/RPC2',)

with SimpleXMLRPCServer(
	('0.0.0.0', 8000),
	RequestHandler,
	logRequests=True,
	allow_none=True
) as server:
	server.register_introspection_functions()
	server.register_instance(connectionInstance)
	server.serve_forever()