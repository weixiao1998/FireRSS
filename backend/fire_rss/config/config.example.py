# config.py example
# NOTE: please change config and save as "config.py"

DOMAIN = "fire-rss.webxiaoweb.top"

# db
DB_ENGINE_CONFIG = {
    "url": "mysql://fire_rss:fire_rss_by_weixiao1998@mysql:3306/fire_rss",
    "pool_recycle": 3600,
}

DB_SESSION_MAKER_CONFIG = {
    "autocommit": False,
}

# cors
CORS_CONFIG = {
    "allow_origins": [
        f"https://{DOMAIN}",
        f"http://{DOMAIN}",
    ],
    "allow_credentials": True,
    "allow_methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    "allow_headers": [],
}
