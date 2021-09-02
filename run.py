import sys

from flaskRest.app import app

PORT = 3200
HOST = '0.0.0.0'

if __name__=="__main__":
	print("Server running in port %s"%(PORT))
	app.run(host=HOST, port=PORT, debug=True)




