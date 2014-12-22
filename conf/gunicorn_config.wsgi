# Gunicorn settings

PROJ_NAME = "k-state-hackathon"

pid = "/tmp/%s.gunicorn.pid" % PROJ_NAME
accesslog = "/tmp/%s.gunicorn.access.log" % PROJ_NAME
errorlog = "/tmp/%s.gunicorn.error.log" % PROJ_NAME
bind = "unix:/tmp/%s.gunicorn.sock" % PROJ_NAME
