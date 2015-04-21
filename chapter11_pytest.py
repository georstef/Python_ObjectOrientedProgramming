
# PLEASE VIEW FILE -> test_chapter11_pytest.py

'''
cmd->cd folder_with_tests->py.test

When we run py.test, it will start in the current folder
and search for any modules in that folder or subpackages
whose names start with the characters test_.
If there are any functions in this module that also start with test,
they will be executed as individual tests.
Further, if there are any classes in the module whose name starts with Test,
any methods on that class that start with test_ will also be executed in the
test environment.

module => test_
function => test
classes => Test
classes methods => test_

py.test suppresses the print methods
to allow print then add -s
eg. py.test test_chapter11_pytest.py -s
'''

def test_int():
    assert True

#gets called before each method (only for module methods like the one above)
def setup_function(function):
    '''
    setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    '''

#gets called after each method (only for module methods like the one above)
def teardown_function(function):
    '''
    teardown any state that was previously setup with a setup_function
    call.
    '''    

#gets called at the begining of each module
def setup_module(module):
    '''
    setup any state specific to the execution of the given module.
    '''

#gets called at the end of each module
def teardown_module(module):
    ''' teardown any state that was previously setup with a setup_module
    method.
    '''
	
class TestNumbers:
    #gets called at the begining of each class
    @classmethod
    def setup_class(cls):
        cls.i = '1'
        '''
		setup any state specific to the execution of the given class (which
		usually contains tests).
		'''

    #gets called at the end of each class
    @classmethod
    def teardown_class(cls):
        '''
        teardown any state that was previously setup with a call to
		setup_class.
		'''

    #gets called before each method
    def setup_method(self, func):
        self.num = 2

    #gets called after each method
    def teardown_method(self, func):
        pass
        
    def test_int_float(self):
        assert 1 == self.num
        
    def test_int_str(self):
        assert 1 == TestNumbers.i
