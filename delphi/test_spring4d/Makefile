all: local remote local_gui remote_gui test_project

local:
	dcc32 \
		-W- \
		-e"Build\Win32" \
		-u"%DELPHI%\source" \
		-u"DependencySource" \
		-u"Source" \
		--default-namespace:System \
		Source\LocalCalculator.dpr

remote:
	dcc32 \
		-W- \
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
		-W- \
		-e"Build\Win32" \
		-u"%DELPHI%\source" \
		-u"DependencySource" \
		-u"Source" \
		--default-namespace:System \
		Source\LocalCalculatorGUI.dpr

remote_gui:
	dcc32 \
		-W- \
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
		-W- \
		-e"Build\Win32" \
		-u"%DELPHI%\source" \
		-u"%DELPHI%\source\soap" \
		-u"%DELPHI%\source\rtl\win" \
		-u"DependencySource" \
		-u"Source" \
		--default-namespace:System \
		Source\CalculatorTest.dpr

osx: osx_local osx_remote osx_local_gui osx_remote_gui

osx_local:
	dccosx \
		-W- \
		-e"Build\MacOSX" \
		-u"%DELPHI%\source" \
		-u"DependencySource" \
		-u"Source" \
		--default-namespace:System \
		Source\LocalCalculator.dpr

osx_remote:
	dccosx \
		-W- \
		-e"Build\MacOSX" \
		-u"%DELPHI%\source" \
		-u"%DELPHI%\source\soap" \
		-u"DependencySource" \
		-u"Source" \
		--default-namespace:System \
		Source\RemoteCalculator.dpr

osx_local_gui:
	dccosx \
		-W- \
		-e"Build\MacOSX" \
		-u"%DELPHI%\source" \
		-u"DependencySource" \
		-u"Source" \
		--default-namespace:System \
		Source\LocalCalculatorGUI.dpr

osx_remote_gui:
	dccosx \
		-W- \
		-e"Build\MacOSX" \
		-u"%DELPHI%\source" \
		-u"%DELPHI%\source\soap" \
		-u"DependencySource" \
		-u"Source" \
		--default-namespace:System \
		Source\RemoteCalculatorGUI.dpr

run:
	Build\Win32\LocalCalculator.exe
	Build\Win32\RemoteCalculator.exe

clean:
	del Build\Win32\*.exe

test:
	Build\Win32\CalculatorTest.exe
