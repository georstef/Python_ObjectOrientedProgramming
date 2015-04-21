'''
cmd-cd folder_with_tests-py.test
if we want to exit after the first failed test then add -x
eg.
cpy.test -x

When we run py.test, it will start in the current folder
and search for any modules in that folder or subpackages
whose names start with the characters test_.
If there are any functions in this module that also start with test,
they will be executed as individual tests.
Further, if there are any classes in the module whose name starts with Test,
any methods on that class that start with test_ will also be executed in the
test environment.

module = test_
function = test
classes = Test
classes methods = test_

py.test suppresses the print methods
to allow print then add -s
eg. py.test test_chapter11_pytest.py -s
'''

#this is a funcarg, to use as datavariables in test functions
#can also be placed in a configuration file named conftest.py
#example to create a variableargument named just_an_int
def pytest_funcarg__just_an_int(request)
    #request.addfinalizer          to be looked up if needed
    #request.cached_setup          to be looked up if needed
    return 4

#use of funcarg
def test_an_int(just_an_int)
    assert just_an_int == 3

#skipped method 1
def test_an_int_to_skip1(just_an_int)
    py.test.skip(just skip)
    assert just_an_int == 2

#skipped method 2
import py.test #is only needed for the next method
@py.test.mark.skipif(sys.version_info.major == 3)
def test_an_int_to_skip2(just_an_int)
    assert just_an_int == 5
#--------------------------------------------------------------------------
#test module method
def test_int()
    assert True

#gets called before each method (only for module methods like the one above)
def setup_function(function)
    '''
    setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    '''

#gets called after each method (only for module methods like the one above)
def teardown_function(function)
    '''
    teardown any state that was previously setup with a setup_function
    call.
    '''    

#--------------------------------------------------------------------------
#gets called at the begining of each module
def setup_module(module)
    '''
    setup any state specific to the execution of the given module.
    '''

#gets called at the end of each module
def teardown_module(module)
    ''' 
	teardown any state that was previously setup with a setup_module
    method.
    '''
	
#--------------------------------------------------------------------------
class TestNumbers
    #gets called at the begining of each class
    @classmethod
    def setup_class(cls)
        cls.i = '1'
        '''
		setup any state specific to the execution of the given class (which
		usually contains tests).
		'''

    #gets called at the end of each class
    @classmethod
    def teardown_class(cls)
        '''
        teardown any state that was previously setup with a call to
		setup_class.
		'''

    #gets called before each method
    def setup_method(self, func)
        self.num = 2

    #gets called after each method
    def teardown_method(self, func)
        pass
        
    def test_int_float(self)
        assert 1 == self.num
        
    def test_int_str(self)
        assert 1 == TestNumbers.i