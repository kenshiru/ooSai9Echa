from aiohttp import web
from app.categories_collection import categories_collection
import logging


async def categories_by_phrase_handler(request):
    """
    Search categories by phrase
    :param request: GET request has query param 'phrase' (category search condition)
    :return: response on category by phrase request
    :rtype: Response
    """
    phrase = request.query.get('phrase')

    if phrase is None:
        return web.json_response({
            'success': False,
            'message': 'Invalid phrase'
        })

    try:
        found_categories = categories_collection.get_categories_by_phrase(phrase)
        return web.json_response({
            "success": True,
            "data": {
                "categories": [category.name for category in found_categories]
            }
        })
    except Exception as error:
        logging.error('Error on category search by phrase:', error)

        return web.json_response({
            'success': False,
            'message': 'internal error %s' % error.message
        })
