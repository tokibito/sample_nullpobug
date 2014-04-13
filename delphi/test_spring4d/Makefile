all: win32

win32:
	dcc32 \
		-e"Build\Win32" \
		-u"%DELPHI%\source" \
		-u"DependencySource" \
		-u"Source" \
		--default-namespace:System \
		Source\Calculator.dpr

run:
	Build\Win32\Calculator.exe

test:
	Build\Win32\CalculatorTest.exe
