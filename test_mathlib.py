import	mathaddsub  # file in current directory that has our 'add' & 'subtract' functions defined
import	mathlibmuldiv  # file in current directory that has our 'multiply' & 'divide' functions defined
import  mathsqrtpwr  # file in current directory that has our 'square root' & 'x to the y power' functions defined
###....add yml file comment to trigger new build...4/2/19
###...add a bogus comment to kickoff a build on jernkins
#..................	V E R Y   I M P O R T A N T   M E S S A G E   B E L O W  ..........
###....The 'pytest' framework execution (THIS) file, along with all functions defined within it 'MUST' start with 'test_'  
#
def	test_calc_add():
	total = mathaddsub.calc_add(4,5)
	assert total == 9
	
def	test_calc_sub():
	total = mathaddsub.calc_sub(4,5)
	assert total == -1

def	test_calc_mult():
	result = mathlibmuldiv.calc_mult(10,3)
	assert result == 30

def	test_calc_div():
	result = mathlibmuldiv.calc_div(10,2)
	assert result == 5
	
def	test_calc_sqrt():
	result = mathsqrtpwr.calc_sqroot(16)
	assert result == 4

def	test_calc_pwr():
	result = mathsqrtpwr.calc_pwr(2,6)
	assert result == 64
	
#
#C:\PythonScripts\pytest_framework>pytest      (you could also type 'python -m pytest' on console command line)
#
#C:\PythonScripts\pytest_framework>pytest
#=============================================================== test session starts ======
#platform win32 -- Python 3.7.1, pytest-4.1.1, py-1.7.0, pluggy-0.8.1
#rootdir: C:\PythonScripts\pytest_framework, inifile:
#collected 4 items
#
#test_mathlib.py ....
#
#============================================================ 4 passed in 0.04 seconds ====
#
###....NOTE: If the 'test_' prefix is missing on incorrectly typed, pytest will ignore it and the test will not get executed
#
###....Output (below), with verbose mode (-v) enabled
#
#C:\PythonScripts\pytest_framework>pytest -v
#=============================================================== test session starts =====================================================
#platform win32 -- Python 3.7.1, pytest-4.1.1, py-1.7.0, pluggy-0.8.1 -- c:\users\jim\appdata\local\programs\python\python37-32\python.exe
#cachedir: .pytest_cache
#rootdir: C:\PythonScripts\pytest_framework, inifile:
#collected 4 items
#
#test_mathlib.py::test_calc_add PASSED
#test_mathlib.py::test_calc_sub PASSED
#test_mathlib.py::test_calc_mult PASSED
#test_mathlib.py::test_calc_div PASSED
#
#============================================================ 4 passed in 0.08 seconds ===================================================
#
