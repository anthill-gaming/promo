"""
Example:

    @app.task(ignore_result=True)
    def your_task():
        ...
"""

from anthill.platform.core.celery import app

# Create your celery tasks here
