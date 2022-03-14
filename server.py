import autoevent

from autoevent import settings
from autoevent import app



if __name__ == '__main__':
    app.run(
        host=settings.Settings().API_HOST,
        port=settings.Settings().API_PORT,
        debug=settings.Settings().API_DEBUG,
        auto_reload=settings.Settings().API_RELOAD,
    )
