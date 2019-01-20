import pandas as pd

"""
Utility Tools 

"""

class UtilTool():

    """
    Read csv file into Pandas DataFrame

    """

    @staticmethod
    def read_to_dataframe(config):
        full_file_name = config.filename
        if config.path is not None:
            full_file_name = config.path + "/" + config.filename
        """
        Assuming that the first line of header...
        """
        df = pd.read_csv(full_file_name)

        return df