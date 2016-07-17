"""This is a test file for setting up git!"""

class TestFile(object):

    def __init__(self):
        """Instantiates Tim."""
        self.testName = 'Tim'

    def firstTestMethod(self):
        """Prints method name"""
        print 'this is the first test method. TestObject is {}'.format(self.testName)

    def secondTestMethod(self, num=2):
        """Prints method name and number"""
        print 'this is the second test method. Number equals {}'.format(num)

if __name__ == '__main__':
    # instantiate our object when the program is run
    testObject = TestFile()
    testObject.firstTestMethod()
