from __future__ import absolute_import

import sys
import copy
import logging

try:
    from itertools import imap
except ImportError:
    imap = map

from tornado import web

from ..views import BaseHandler
from ..utils.results import get_results_by_taskid, get_results

logger = logging.getLogger(__name__)


class ResultView(BaseHandler):
    @web.authenticated
    def get(self, task_id):
        result = get_results_by_taskid(task_id)
        if result is None:
            raise web.HTTPError(404, "Unknown task '%s'" % task_id)
        self.render("result.html", result=result, childs=childs)


class ResultsView(BaseHandler):
    @web.authenticated
    def get(self):
        results = get_results(self.application.events)
        self.render(
            "results.html",
            results=[],
            columns=app.options.tasks_columns,
            time=time,)
