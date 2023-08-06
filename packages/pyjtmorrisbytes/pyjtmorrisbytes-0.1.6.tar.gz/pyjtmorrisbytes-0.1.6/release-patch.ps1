
$currentDir = Split-Path $MyInvocation.MyCommand.Path
Start-Process powershell.exe './scripts/build/build-cython.ps1' -Wait -WorkingDirectory $currentDir -NoNewWindow
Start-Process  'tox' -Wait -WorkingDirectory $currentDir -NoNewWindow
Start-Process powershell.exe './scripts/build/build-docs.ps1' -Wait -WorkingDirectory $currentDir -NoNewWindow
Invoke-Expression "git add -A"
Invoke-Expression "git commit -m 'making automatic release'"
Invoke-Expression '.\setup.py version --bump patch --commit'
Invoke-Expression 'rm ./dist/*.whl'
Invoke-Expression 'rm ./dist/*.tar.gz'
Invoke-Expression 'rm ./dist/*.zip'
Start-Process powershell.exe './scripts/build/make-dist.ps1' -Wait -WorkingDirectory $currentDir -NoNewWindow