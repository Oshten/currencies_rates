import logging
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from apps.redis.scripts import get_rates_from_redis


router = APIRouter()


@router.get('/courses')
def get_all_courses():
    try:
        rates = get_rates_from_redis()
    except Exception as exc:
        logging.error(f'Server redis is unavailable. Error {exc}')
        response = JSONResponse(content={'error': 'Not found'})
        response.status_code = 404
        return response
    return rates


@router.get('/{pair_name}')
def get_course(pair_name: str):
    course = get_rates_from_redis(pair_name)
    if course.get(pair_name):
        return course
    response = JSONResponse(content={'error': f'{pair_name} not found'})
    response.status_code = 404
    return response