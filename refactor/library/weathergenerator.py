from refactor.contract.process import Process


class WeatherGeneratorProcess(Process):

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
