from refactor.contract.factory import SimulatorFactoryReporterInterface
from refactor.constant import ReporterType
from refactor.simulation.filereporter import FileBasedReporter
from refactor.simulation.stringreporter import StringBasedReporter
from refactor.simerror.unknown import UnknownReporterException
from refactor.simerror.unknown import UnknownConfigException
from refactor.simlog.printlog import printlog


class SimulatorReporterFactory(SimulatorFactoryReporterInterface):

    def __init__(self, conf):
        self.simulation_report = conf

    def get_reporter(self):

        if self.simulation_report is None:
            raise UnknownConfigException("Config given to SimulatorReporterFactory is None")

        printlog("SimulatorReporterFactory","Using reporter {}".format(self.simulation_report["type"]))

        if self.simulation_report["type"] == ReporterType.FILE_BASED.value:
            reporter = FileBasedReporter(self.simulation_report)
        elif self.simulation_report["type"] == ReporterType.STRING_BASED.value:
            reporter = StringBasedReporter(self.simulation_report)
        else:
            raise UnknownReporterException("The reporter type {} is not implemented".format(self.simulation_report["type"]))

        return reporter
