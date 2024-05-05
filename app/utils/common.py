import hashlib
import base64
import time
from datetime import datetime

from sanic import Request
from sanic.response import json
from sanic.exceptions import Unauthorized

def get_ttl_hash(seconds=3600):
    return round(time.time() / seconds)

def append_query_param(url, query_param):
    if query_param:
        delimiter = "&" if "?" in url else "?"
        url += delimiter + query_param
    return url


async def get_authorized_user(request: Request):
    user = request.ctx.user
    if not user:
        # Todo: check permissions here
        raise Unauthorized(message=str("Not Authorized"))
    return user


def response(data, code=200, meta=None, headers=None):
    body = dict(data=data, is_success=code == 200, status=code)
    if meta:
        body['meta'] = meta

    return json(body=body, status=code, headers=headers)


def get_hash(word):
    md5pass = hashlib.md5(bytes(word, encoding="utf-8")).digest()
    return base64.b64encode(md5pass).decode("utf-8")


def obj_to_dict(obj, keys=None):
    if not keys:
        return obj.__dict__
    result = dict()
    for key in keys:
        result[key] = getattr(obj, key)

    return result


def timestamp_str():
    return datetime.now().strftime("%d%m%Y%H%M%S%f")


def timestamp_int():
    return int(datetime.now().strftime("%d%m%Y%H%M%S%f"))


async def list_objects_from_queryset(queryset, filters, order_by, limit, offset, is_to_dict=True, serialize_keys=None):
    if filters:
        queryset = queryset.filter(**filters)
    if limit:
        queryset = queryset.limit(limit)
    if offset:
        queryset = queryset.offset(offset)
    if order_by:
        queryset = queryset.order_by(*order_by)
    else:
        queryset = queryset.order_by('-updated_at')
    result_set = await queryset
    if is_to_dict:
        result_set = [result.to_dict(serialize_keys=serialize_keys) for result in result_set]
    return result_set or []


async def list_objects_from_queryset_paginated(queryset, filters, order_by, page, page_size=10, is_to_dict=True, serialize_keys=None):
    total = await queryset.count()
    offset = (page - 1) * page_size
    limit = page * page_size
    items = await list_objects_from_queryset(queryset, filters, order_by, limit, offset, is_to_dict, serialize_keys)
    return dict(
        items=items,
        pagination=dict(
            total=total,
            page=page,
            page_size=page_size
        )
    )
