from refactor.contract.formater import FormatterInterface


class PipeFormatter(FormatterInterface):

    def __init__(self, keys_used, keys_separator):
        """
        Pipe Formatter separates each value of key by "|"
        e.g.
        Vancouver|49.24|-123.12|10|2019-02-13T22:37:46.806427+00:00|Sunny|10|1200|20

        :param keys_used: values to keys to extract
        :param keys_separator: This parameter is ignored for this formatter type
        """
        self.key_used = keys_used
        self.delimiter = "|"

    def __call__(self, state):
        """

        :param state: pd.Series with key pair values
        :return: formatted string output
        """
        arr_key_values = state.repr(self.key_used)
        return self.delimiter.join(arr_key_values)