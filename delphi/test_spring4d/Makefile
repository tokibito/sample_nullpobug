all: local remote local_gui test_project

local:
	dcc32 \
		-e"Build\Win32" \
		-u"%DELPHI%\source" \
		-u"DependencySource" \
		-u"Source" \
		--default-namespace:System \
		Source\LocalCalculator.dpr

remote:
	dcc32 \
		-e"Build\Win32" \
		-u"%DELPHI%\source" \
		-u"%DELPHI%\source\soap" \
		-u"%DELPHI%\source\rtl\win" \
		-u"DependencySource" \
		-u"Source" \
		--default-namespace:System \
		Source\RemoteCalculator.dpr

local_gui:
	dcc32 \
		-e"Build\Win32" \
		-u"%DELPHI%\source" \
		-u"DependencySource" \
		-u"Source" \
		--default-namespace:System \
		Source\LocalCalculatorGUI.dpr

remote_gui:
	dcc32 \
		-e"Build\Win32" \
		-u"%DELPHI%\source" \
		-u"%DELPHI%\source\soap" \
		-u"%DELPHI%\source\rtl\win" \
		-u"DependencySource" \
		-u"Source" \
		--default-namespace:System \
		Source\RemoteCalculatorGUI.dpr

test_project:
	dcc32 \
		-$M+ \
		-e"Build\Win32" \
		-u"%DELPHI%\source" \
		-u"%DELPHI%\source\soap" \
		-u"%DELPHI%\source\rtl\win" \
		-u"DependencySource" \
		-u"Source" \
		--default-namespace:System \
		Source\CalculatorTest.dpr

run:
	Build\Win32\LocalCalculator.exe
	Build\Win32\RemoteCalculator.exe

clean:
	del Build\Win32\*.exe

test:
	Build\Win32\CalculatorTest.exe
