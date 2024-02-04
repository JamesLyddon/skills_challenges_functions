class GrammarStats:
    _END_CHARS = ('.', '?', '!')
    def __init__(self):
        self.tests = 0
        self.passed = 0

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        if type(text) != str or not len(text):
            raise Exception("Text input must be a non-empty string.")
        self.tests += 1
        if text[0].isupper() and text[-1] in self._END_CHARS:
            self.passed += 1
            return True
        return False

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        if self.tests == 0:
            raise Exception("You haven't checked any sentences yet.")
        elif self.passed == 0:
            return 0
        return int(self.passed / self.tests * 100)
