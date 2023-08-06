"""Submission core configuration parameters."""

import os
from kombu.serialization import register
from .serializer import dumps, loads

register('ejson', dumps, loads,
         content_type='application/x-ejson',
         content_encoding='utf-8')

APPLY_RULES = bool(int(os.environ.get('APPLY_RULES', '1')))
BROKER_URL = os.environ.get('SUBMISSION_BROKER_URL', 'redis://localhost/0')
RESULT_BACKEND = os.environ.get('SUBMISSION_RESULT_BACKEND', BROKER_URL)
QUEUE_NAME_PREFIX = os.environ.get('SUBMISSION_QUEUE_NAME_PREFIX',
                                   'submission-')
PREFETCH_MULTIPLIER = int(os.environ.get(
    'SUBMISSION_WORKER_PREFETCH_MULTIPLIER',
    '1'
))
TASK_ACKS_LATE = bool(int(os.environ.get('SUBMISSION_TASK_ACKS_LATE', '1')))

CELERY_ACCEPT_CONTENT = ['ejson']
CELERY_TASK_SERIALIZER = 'ejson'
CELERY_RESULT_SERIALIZER = 'ejson'


ENABLE_ASYNC = os.environ.get('ENABLE_ASYNC', '0')
"""
If ``1``, asynchronous callbacks will be dispatched to the worker.

Otherwise they will be executed in the thread in which they are called.
"""

ENABLE_CALLBACKS = os.environ.get('ENABLE_CALLBACKS', '0')
"""If ``0``, callbacks bound to events will not be executed."""
