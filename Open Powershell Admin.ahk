#NoEnv
#SingleInstance force
SetKeyDelay, 60
BlockInput, On

; WinGet, SavedWinId, ID, A ;Save our current active window

; if WinExist("ALJI") {
	; MsgBox "Found ALJI window..."
	; WinActivate
Send {AltDown}f{AltUp}sa
; } else {
; 	MsgBox "No ALJI window found..."
; }

; WinActivate ahk_id %SavedWinId%  ;Restore original window
BlockInput, Off
ExitApp