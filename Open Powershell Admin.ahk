#NoEnv
#SingleInstance force
SetKeyDelay, 60
BlockInput, On

if mustOpenWindow("ALJI") {
	Send {AltDown}f{AltUp}sa
}

if A_IsAdmin {
	if mustOpenWindow("Administrator: Windows PowerShell") {
		SetKeyDelay, 10
		Send env/Scripts/activate{Enter}
	} 
} else {
	MsgBox, No admin privlidges.  Must run env/Scripts/activate
}

mustOpenWindow(wName) {
	waitSecs := 2
	WinWait, %wName%, , waitSecs 
	if WinExist(wName){
		WinActivate
		WinWaitActive %wName%, , waitSecs
		return True
	} else {
		MsgBox No %wName% window found... exiting...
		ExitApp 1
	}
}

BlockInput, Off
ExitApp