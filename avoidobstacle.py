from timeit import default_timer


class AvoidObstacle:

    def __init__(self):
        self.start_time = None
        self.runtime = 0
        self.motor_recommendation = (None, None)
        self.is_started = False


    def left(self):
        self.motor_recommendation = (1.0, -0.5)


    def right(self):
        self.motor_recommendation = (-0.5, 1.0)


    def forward(self):
        self.motor_recommendation = (1.0, 1.0)


    def reset(self):
        self.runtime = 0
        self.start_time = None
        self.is_started = False

    def start(self):
        self.start_time = default_timer()
        self.is_started = True

    def update(self):
        if not self.is_started:
            self.start()
        self.runtime = default_timer() - self.start_time
        if self.runtime < 1:
            self.left()
        elif self.runtime < 4:
            self.forward()
        elif self.rutime < 5:
            self.right()
        elif self.runtime < 8:
            self.forward()
        elif self.runtime < 9:
            self.right()
        elif self.runtime < 12:
            self.forward()
        elif self.runtime < 13:
            self.left()
        else: self.reset()

    def get_runtime(self):
        return default_timer - self.start_time
