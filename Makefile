PY = python3
# PY = py -3.7 # for windows - ensure python version 3.7 
# PY = python3   # for linux
# PY = python3.8 # for linux - ensure python version 3.8

PYINSTALLER = pyinstaller

APPNAME = rconclient
BINNAME = $(APPNAME)


ifeq ($(OS),Windows_NT)
	EXE = .exe
endif

_build: pre-build build

run:
	$(PY) $(CURDIR)/$(APPNAME)/main.py $(ARGS)

deps:
	$(PY) -m pip install -U -r $(CURDIR)/requirements.txt

deps-user:
	$(PY) -m pip install -U -r --user $(CURDIR)/requirements.txt

pre-build:
	$(PY) -m pip install -U --user $(PYINSTALLER)

build:
	$(PYINSTALLER) $(CURDIR)/$(APPNAME)/main.py \
		-y --onefile \
		--name $(BINNAME)$(EXE)

install:
	mv $(CURDIR)/dist/$(BINNAME) \
		/usr/bin/$(BINNAME)
	chmod +x /usr/bin/$(BINNAME)

.PHONY: run deps deps-user pre-build build _build