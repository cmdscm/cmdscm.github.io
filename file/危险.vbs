Set WshShell= WScript.CreateObject("WScript.Shell")
WshShell.AppActivate ""
for i=1 to 150
WScript.Sleep 450
WshShell.SendKeys "^v"
WshShell.SendKeys "%s"
Next