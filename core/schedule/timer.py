import time
from repeaters import REPEATER_REGISTRY


class ScheduledTask:
    command = ''
    next_launch = None
    repeater = None

    def __init__(self, command, repeater, **kwargs):
        self.command = command
        self.repeater = REPEATER_REGISTRY[repeater]()
        self.next_launch = self.repeater.schedule_next_launch(init=True, **kwargs)

    def get_command(self):
        if self.next_launch and time.time() >= self.next_launch:
            self.next_launch = self.repeater.schedule_next_launch()
            return self.command
        return None


class Timer():
    tasks = {}
    repeaters = None

    def __init__(self, tasks):
        for task in tasks:
            self.add_task(task)

    def iterate(self):
        for name, task in self.tasks.iteritems():
            command = self.tasks[name].get_command()
            if command:
                return command
        return False

    def add_task(self, task, replace=False):
        """
        adds task to shedule.
        :param task: dict with task, as in configuration
        :param replace: boolean. if true - will rewrite existing task with given name
        :return: True if created/rewritten, False if existing and not rewritten
        """
        if not task['name'] in self.tasks or replace:
            self.tasks[task['name']] = ScheduledTask(task['command'], task['repeater'], **task['params'])
            return True
        return False
