from typing import Dict, List

from dogebuild.relations import TaskRelationManager


class Context:
    def __init__(self, phases: Dict[str, List[str]] = None):
        self.relman = TaskRelationManager(phases)
        self.plugins = []
        self.dependencies = []
        self.test_dependencies = []


class ContextHolder:
    CONTEXT = None

    @staticmethod
    def create(phases=None):
        ContextHolder.CONTEXT = Context(phases)

    @staticmethod
    def clear_and_get():
        context = ContextHolder.CONTEXT
        ContextHolder.CONTEXT = None
        return context


def rewrite_phases(phases: Dict[str, List[str]] = None):
    ContextHolder.create(phases)
