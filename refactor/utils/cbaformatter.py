from refactor.contract.formater import FormatterInterface
from refactor.constant import CBA_TEMP_FORMAT


class CBAFormatter(FormatterInterface):

    def __init__(self, keys_used, keys_separator):
        """
        CBA Client wants weather data in a particular format
        Vancouver|49.24,-123.12,10|2019-02-13T22:37:46.810594+00:00|Sunny|+20|1200|20

        This class takes care of this format.
        This class is sort of closed to modification but open for extension or adding new format types.
        Each format class should implement FormatterInterface
        Here we assign "delimiter" which will be separating each fields
        and also if temperature value is > 0 then put "+"
        Since the design doesnt decide of any particular sequence to extract information which is given by the user of
        this class
        :param keys_used: List of keys for which value
        """
        self.key_used = keys_used
        self.delimiter = keys_separator
        difflen = len(self.key_used) - (len(self.delimiter) + 1)

        """
        A solution for case where the number of keys for which value needs to be extracted is more than number of 
        delimiter separating them.
        Append  "|" so that all values for which delimiters isnt mentioned.
        """
        self.delimiter = self.delimiter + ["|"]* difflen if difflen > 0  else self.delimiter

        self.temp_formatting = keys_used.index("temperature") if "temperature" in keys_used else -1

    def __call__(self, state):
        """
        It pulls of values of keys mentioned in key_used from state object.
        Since CBA Client wants output in a particular format it adds delimiter after value
        values Vancouver and 49.24 are separated by "|"
        while 49.24 and -123.12 by ","
        e.g [Vancouver "|" 49.24 "," -123.12 "," 10 "|" 2019-02-13T23:58:55.807253+00:00 "|" Sunny "|"-20 "|" 1200 "|" 20]
        :param state: pd.Series with key pair values
        :return: formatted string output
        """
        arr_key_values = state.repr(self.key_used)

        if self.temp_formatting == 0:
            formatted_array = [CBA_TEMP_FORMAT + arr_key_values[0]]
        else:
            formatted_array = [arr_key_values[0]]

        ind = 1
        for val, delimiter in zip(arr_key_values[1:], self.delimiter):
            formatted_array.append(delimiter)
            if self.temp_formatting != -1 and self.temp_formatting == ind and float(val) > 0.0:
                formatted_array.append(CBA_TEMP_FORMAT)
            formatted_array.append(val)
            ind = ind + 1

        return "".join(formatted_array)