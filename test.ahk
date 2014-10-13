;------------------------------------------------------------------------
; Ctrl+Alt+Space - Always on top current window
;------------------------------------------------------------------------
^!SPACE:: Winset, Alwaysontop, , A

;------------------------------------------------------------------------
; Ctrl+Alt+Arrows  - Move the current window by a small amount
;------------------------------------------------------------------------
^!+Up::
	WinGet, hwnd, ID, A
	WinGetPos, X, Y, Width, Height, ahk_id %hwnd%
	WinMove, ahk_id %hwnd%,, X, Y-25, Width, Height
return

^!+Down::
	WinGet, hwnd, ID, A
	WinGetPos, X, Y, Width, Height, ahk_id %hwnd%
	WinMove, ahk_id %hwnd%,, X, Y+25, Width, Height
return

^!+Right::
	WinGet, hwnd, ID, A
	WinGetPos, X, Y, Width, Height, ahk_id %hwnd%
	WinMove, ahk_id %hwnd%,, X+25, Y, Width, Height
return

^!+Left::
	WinGet, hwnd, ID, A
	WinGetPos, X, Y, Width, Height, ahk_id %hwnd%
	WinMove, ahk_id %hwnd%,, X-25, Y, Width, Height
return

^t::run, explore C:\byRainProgram\TRTN