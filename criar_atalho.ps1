$WshShell = New-Object -comObject WScript.Shell
$Shortcut = $WshShell.CreateShortcut("$Home\Desktop\DeepCode AI.lnk")
$Shortcut.TargetPath = "C:\Users\FABIO\Desktop\PROJETOS\DEEPCODE\INICIAR_DEEPCODE.bat"
$Shortcut.WorkingDirectory = "C:\Users\FABIO\Desktop\PROJETOS\DEEPCODE"
$Shortcut.Save()
Write-Host "Atalho criado na Area de Trabalho!"
