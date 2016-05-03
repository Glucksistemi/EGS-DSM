import time


class ScheduleRepeater:
    def __init__(self, **kwargs):
        pass

    def schedule_next_launch(self, init=False, **kwargs):
        return 0


class IntervalRepeater(ScheduleRepeater):
    interval = None

    def schedule_next_launch(self, init=False, **kwargs):
        if not self.interval:
            if not kwargs.get('interval', False):
                return None
            self.interval = kwargs['interval']
        delay = kwargs.get('delay', 0)
        return time.time() + delay + self.interval


class OnceRepeater(ScheduleRepeater):
    def schedule_next_launch(self, init=False, **kwargs):
        if init:
            try:
                return time.mktime(time.strptime(kwargs['datetime'], '%d-%m-%Y %H:%M:%S'))
            except:
                return None
        else:
            return None


# keep this constant beneath classes.
# register every class here
REPEATER_REGISTRY = {
    'interval': IntervalRepeater,
    'once': OnceRepeater
}