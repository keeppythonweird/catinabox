@echo off
set "VIRTUAL_ENV=C:\Users\Ann\Documents\GitHub\catinabox\catpy"

if defined _OLD_VIRTUAL_PROMPT (
    set "PROMPT=%_OLD_VIRTUAL_PROMPT%"
) else (
    if not defined PROMPT (
        set "PROMPT=$P$G"
    )
	set "_OLD_VIRTUAL_PROMPT=%PROMPT%"	
)
set "PROMPT=(catpy) %PROMPT%"

if not defined _OLD_VIRTUAL_PYTHONHOME (
    set "_OLD_VIRTUAL_PYTHONHOME=%PYTHONHOME%"
)
set PYTHONHOME=

if defined _OLD_VIRTUAL_PATH (
    set "PATH=%_OLD_VIRTUAL_PATH%"
) else (
    set "_OLD_VIRTUAL_PATH=%PATH%"
)
set "PATH=%VIRTUAL_ENV%\Scripts;%PATH%"

:END
