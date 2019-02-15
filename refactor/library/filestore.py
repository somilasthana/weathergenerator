from refactor.contract.report import TaskOutputHandler


class FileStoreTaskOutputHandler(TaskOutputHandler):

    def __init__(self, file_details):
        self.file_details = file_details
        self._handler = open(self.file_details.filename, self.file_details.mode)

    def save_state(self, state):
        pass

    def cleanup(self):
        self._handler.close()