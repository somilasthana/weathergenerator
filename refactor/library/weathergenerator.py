from refactor.contract.process import Process


class WeatherGeneratorProcess(Process):
    """
    This is interface that Simulator enforces when it add tasks to its list to run.
    Simulator expects each task that is added to the its internal list will implement run_method and get_state
    """

    def __init__(self, weather_algorithm):
        self.weather_algorithm = weather_algorithm
        self.weather_algorithm.init()
        self.state = None

    def run_method(self):
        self.state = next(self.weather_algorithm.run())

    def get_state(self):
        return self.state

    def cleanup(self):
        self.weather_algorithm.cleanup()

    def __repr__(self):
        return "Generator uses Algorithm" + self.weather_algorithm.__repr__()
