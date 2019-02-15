from refactor.contract.report import SimulatorReporterInterface


class StringBasedReporter(SimulatorReporterInterface):

    def __init__(self, reporter_config):
        """
        Extracts path and filename from config object
        For Filebased  opens the filename for writing or appending ( depending on "mode" )
        keylist : list of keys of interest to save
        delimiter used to delimit values before writing
        Suppose we are interested in writing
        :param reporter_config:
        """
        self.string_save = None
        self.reporter_config = reporter_config

    def save_state(self, state):
        self.string_save = str(state)

    def cleanup(self):
        pass