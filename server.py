from aiohttp import web
from app import handlers

app = web.Application()

app.router.add_get('/categories', handlers.categories_by_phrase_handler)

web.run_app(app, host='0.0.0.0', port=5000)
