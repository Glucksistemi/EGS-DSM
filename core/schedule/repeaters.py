import time


class ScheduleRepeater:
    def __init__(self, **kwargs):
        pass

    def schedule_next_launch(self, **kwargs):
        return 0


class IntervalRepeater(ScheduleRepeater):
    interval = None

    def schedule_next_launch(self, **kwargs):
        if not self.interval:
            if not kwargs.get('interval', False):
                return None
            self.interval = kwargs['interval']
        return time.time() + self.interval


# keep this constant beneath classes.
# register every class here
REPEATER_REGISTRY = {
    'interval': IntervalRepeater,
}