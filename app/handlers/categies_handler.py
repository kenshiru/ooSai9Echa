from aiohttp import web


async def categories_handler(request):
    phrase = request.query.get('phrase')

    if phrase is None:
        return web.json_response({
            'success': False,
            'message': 'Invalid phrase'
        })

    return web.json_response({
        "success": True,
        "data": {
            "categories": [1, 2, 3]
        }
    })
