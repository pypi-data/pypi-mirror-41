# -*- coding: utf-8 -*-

"""Collection of useful http error for the Api"""


class GKJsonApiException(Exception):
    """Base exception class for unknown errors"""

    title = 'Unknown error'
    status = '500'
    source = None

    def __init__(self, detail, source=None, title=None, status=None, code=None, id_=None, links=None, meta=None):
        """Initialize a jsonapi exception

        :param dict source: the source of the error
        :param str detail: the detail of the error
        """
        self.detail = detail
        self.source = source
        self.code = code
        self.id = id_
        self.links = links or {}
        self.meta = meta or {}
        if title is not None:
            self.title = title
        if status is not None:
            self.status = status

    def to_dict(self):
        """Return values of each fields of an jsonapi error"""
        error_dict = {}
        for field in ('status', 'source', 'title', 'detail', 'id', 'code', 'links', 'meta'):
            if getattr(self, field, None):
                error_dict.update({field: getattr(self, field)})

        return error_dict


class GKUnprocessableEntity(GKJsonApiException):
    title = "Unprocessable Entity"
    status = '422'

