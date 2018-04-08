import os
# Application配置参数
setting = {
    "static_path": os.path.join(os.path.dirname(__file__), 'static'),
    "template_path": os.path.join(os.path.dirname(__file__), 'template'),
    "cookie_secret": "VwlgCx2uQOqb/5to6oowxh0OWKT/a0egsQTXt2DUrhg=",
    "xsrf_cookies": True,
    "debug": True,
}

# mysql
mysql_options = dict(
    host="127.0.0.1",
    database="ihome",
    user="root",
    password="root"
)

# redis
redis_options = dict(
    host="127.0.0.1",
    port=6379,
)

log_file = os.path.join(os.path.dirname(__file__), 'logs/log')
log_level = "debug"
