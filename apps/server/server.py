import logging
from fastapi import FastAPI

from apps.server.route import router
from apps.logging.logger import handler
from docs.config import LEVEL_LOGGING

def get_applications() -> FastAPI:
    """Create application"""

    application = FastAPI()
    application.include_router(router)
    logging.info('Server started')
    return application


logging.basicConfig(handlers=[handler], level=LEVEL_LOGGING)
app = get_applications()