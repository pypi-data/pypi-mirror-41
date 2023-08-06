# The script use for the development environment

$env:FLASK_ENV='development'
$env:ENV='development'
$env:FLASK_DEBUG="True"
$env:TEST_ENVIORONMENT_VARIABLES="Testing From Windows Powershell"
$env:APP_NAME="pyjtmorrisbytes"
$env:SQL_ALCHEMY_DATBASE_URL = "sqlite:///develop-pyjtmorrisbytes.testdb"

Invoke-Expression "pipenv lock"
Invoke-Expression "pipenv sync"
Invoke-Command .\scripts\build\build_cython.ps1
Invoke-Expression "tox"
Invoke-Expression "setup.py version --bump patch --commit"