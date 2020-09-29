# AGENDA : Pytest FrameWork and Organizg the testing


1. Pytest installation (https://docs.pytest.org/en/stable/)
2. pytest project - SampleFramework

3. create your first tests sample files 
	How pytest identifies the test files and test methods
	- Naming your files >> test_name.py or name_test.py
	- naming your functions >> test_function_name
	
4. Assertation in your tests
    use exression that returns True/False
        assert <expression>, "message if Fails"
        
    to assert the expression is False use 'not' keyword.
        assert not <expression>

5. 	Configure pytest runner in Pycharm: 
	- Please go to File | Settings | Tools | Python Integrated Tools and change the default test runner to pytest. Then you'll get the py.test option to create tests instead of the unittest one.
	
	Run multiple tests from a specific file and multiple files.
	a. Running the specific test file: 
	    '-s' - includes your STDOUT statements (print statements)            
        ```
        pytest -v -s test_sample1.py
        ```
    b. running the single test function (scenario):
        ```
        pytest -v -s test_sample1.py::test_scenario1
        ```
		
	c. Run tests by substring matching
		pytest -k method1 -v
		-k <expression> is used to represent the substring to match
		-v increases the verbosity
        ```
        pytest -k scenario1
        ```

	d. Run tests by markers
		@pytest.mark.<name>.
		pytest -m <name>
		-m <name> mentions the marker name
	   Run disabling the pytest warnings: 
        ```
        pytest -m regression --disable-pytest-warnings
        ```
    e. You can skip the test with @pytest.mark.skip
        
      
      
6. Pytest Fixture: (https://docs.pytest.org/en/stable/fixture.html#fixtures)

	**Fixtures as Function arguments
	```python
	@pytest.fixture
	```
	
	**Fixtures: a prime example of dependency injection
	Fixtures allow test functions to easily receive and work against specific pre-initialized application objects without having to care about import/setup/cleanup details. It’s a prime example of dependency injection where fixture functions take the role of the injector and test functions are the consumers of fixture objects.
	
7. conftest.py: sharing fixture functions
	If during implementing your tests you realize that you want to use a fixture function from multiple test files you can move it to a conftest.py file. You don’t need to import the fixture you want to use in a test, it automatically gets discovered by pytest. The discovery of fixture functions starts at test classes, then test modules, then conftest.py files and finally builtin and third party plugins.
	
	
	**Scope: sharing fixtures across classes, modules, packages or session
	Fixtures requiring network access depend on connectivity and are usually time-expensive to create. Extending the previous example, we can add a scope="module" parameter to the @pytest.fixture invocation to cause the decorated smtp_connection fixture function to only be invoked once per test module (the default is to invoke once per test function).
	
	**Fixture scopes
	Fixtures are created when first requested by a test, and are destroyed based on their scope:

		function: the default scope, the fixture is destroyed at the end of the test.
		class: the fixture is destroyed during teardown of the last test in the class.
		module: the fixture is destroyed during teardown of the last test in the module.
		package: the fixture is destroyed during teardown of the last test in the package.
		session: the fixture is destroyed at the end of the test session.


	**Fixture finalization / executing teardown code
	pytest supports execution of fixture specific finalization code when the fixture goes out of scope. By using a yield statement instead of return, all the code after the yield statement serves as the teardown code:
	
	```python
	# content of conftest.py

	import smtplib
	import pytest


	@pytest.fixture(scope="module")
	def setup():
		print("setup *********")
		element = driver.find_element_by_xpath(xpath)
		
		yield driver  # provide the fixture value
		print("teardown *********")
		driver.close()
	```
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	