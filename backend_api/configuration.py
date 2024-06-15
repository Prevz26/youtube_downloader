# gunicorn_config.py

# Address and port to bind to
bind = '127.0.0.1:8000'

# Number of worker processes
workers = 4

# Maximum number of requests a worker will process before restarting
max_requests = 1000

# Timeout for worker processes in seconds
timeout = 30

# Enable/disable daemon mode
daemon = True
