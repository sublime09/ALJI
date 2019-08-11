#NoEnv
#SingleInstance force
SendMode, Input

if mustOpenWindow("ALJI") {
	SetKeyDelay, 60
	Send {AltDown}f{AltUp}sa
}

if mustOpenWindow("Administrator: Windows PowerShell") {
	winWidth = 400
	xPos = A_ScreenWidth - winWidth
	WinMove, xPos, 0, winWidth, A_ScreenHeight+50
	if A_IsAdmin {
		SetKeyDelay, 10
		Send env/Scripts/activate{Enter}
	} else {
		MsgBox, No admin privlidges.  Must run env/Scripts/activate
	} 
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

ExitApp