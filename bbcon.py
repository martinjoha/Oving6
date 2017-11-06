import time

class BBCON:

    def __init__(self, behaviors, active_behaviors, sensobs, motobs, arbitrator, current_timestep=None, inactive_bahaviors=None, controlled_robot=None):
        self.behaviors = behaviors
        self.active_behaviors = active_behaviors
        self.sensobs = sensobs
        self.motobs = motobs
        self.arbitrator = arbitrator
        self.current_timestep = current_timestep
        self.inactive_behaviors = inactive_bahaviors
        self.controlled_robot = controlled_robot

    def add_behavior(self, behavior):
        self.behaviors.append(behavior)

    def add_sensob(self, sensor):
        self.sensobs.append(sensor)

    def activate_behavior(self, behavior):
        self.active_behaviors.append(behavior)

    def deactivate_behavior(self, behavior):
        self.active_behaviors.remove(behavior)

    def run_one_timestep(self):
        for sensor in self.sensobs:
            sensor.update()
        for behavior in self.behaviors:
            behavior.update()
        (motor_recommendations, halt_flag) = self.arbitrator.choose_action()
        self.motobs.update(motor_recommendations)
        time.sleep(0.5)
        for sensor in self.sensobs:
            sensor.reset()

    #1. behaviors - a list of all the behavior objects used by the bbcon
    #2. active-behaviors - a list of all behaviors that are currently active.
    #3. sensobs - a list of all sensory objects used by the bbcon
    #4. motobs - a list of all motor objects used by the bbcon
    #5. arbitrator - the arbitrator object that will resolve actuator requests produced by the behaviors.

