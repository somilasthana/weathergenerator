from refactor.contract.report import SimulatorReporterInterface
from refactor.utils.pipeformatter import PipeFormatter
from refactor.utils.cbaformatter import CBAFormatter
from refactor.constant import FormatterType
from refactor.simlog.printlog import printlog
from refactor.simerror.unknown import UnknownFileException

class FileBasedReporter(SimulatorReporterInterface):

    def __init__(self, reporter_config):
        """
        Extracts path and filename from config object
        For Filebased  opens the filename for writing or appending ( depending on "mode" )
        keylist : list of keys of interest to save
        delimiter used to delimit values before writing
        Suppose we are interested in writing
        :param reporter_config:
        """
        self.reporter_config = reporter_config
        self.filename = self.reporter_config["details"]["path"] + "/" + self.reporter_config["details"]["filename"]

        try:
            self.fp = open(self.filename, self.reporter_config["details"]["mode"])
        except FileNotFoundError:
            printlog("FileBasedReporter", "Filepath provided doesnt exist {}".format(self.filename))
            raise UnknownFileException("Filepath provided doesnt exist {}".format(self.filename))

        self.keys_used = self.reporter_config["details"]["keys"]

        self.delimiter_type = self.reporter_config["details"]["delimiter_type"]

        self.keys_separator = None
        if "keys_separator" in self.reporter_config["details"]:
            self.keys_separator = self.reporter_config["details"]["keys_separator"]

        self.formatter = None
        if self.delimiter_type == FormatterType.PIPE_TYPE.value:
            self.formatter = PipeFormatter(self.keys_used, self.keys_separator)
        elif self.delimiter_type == FormatterType.CBA_TYPE.value:
            self.formatter = CBAFormatter(self.keys_used, self.keys_separator)

    def save_state(self, state):
        """
        Persists the state in a file, if formatter is not assigned then it simply dumps the state object into a file.
        :param state: pd.Series with key pair values
        :return: None
        """
        if self.formatter is None:
            self.fp.write(str(state))
        else:
            self.fp.write(self.formatter(state))
        self.fp.write('\n')

    def cleanup(self):
        """
        Close the file handle
        :return: None
        """
        self.fp.close()
