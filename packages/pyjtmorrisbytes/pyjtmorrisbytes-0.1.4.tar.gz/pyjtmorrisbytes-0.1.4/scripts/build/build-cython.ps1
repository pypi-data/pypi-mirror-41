
python ./scripts/build/find-cython.py
$cythonfiles = Get-Content ".\cython-files.txt"

Start-Process "cython -3 -a -i -v $cythonfiles" -WorkingDirectory "$PWD"
Start-Process "cythonize -a -i -3 $cythonfiles" -WorkingDirectory "{$PWD}"

# Invoke-Expression "git push"