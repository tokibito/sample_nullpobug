all: win32 osx

win32:
	dcc32 mylib.dpr
	dcc32 dynamic_loading.dpr

osx:
	dccosx mylib.dpr
	dccosx dynamic_loading.dpr

clean:
	del mylib.dll
	del dynamic_loading.exe
	del mylib.dylib
	del dynamic_loading
	del MyLibrary.dcu
