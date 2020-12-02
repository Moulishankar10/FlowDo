Write-Output "FlowDo Autorun Script for Windows"
Write-Output "Checking for Python installation"
$res = Read-Host "Have you installed Python? (Y/N)"
if ( $res -eq "N" -OR "n")
{
    Invoke-WebRequest -Uri https://www.python.org/ftp/python/3.9.0/python-3.9.0-amd64.exe
    ./python-3.9.0-amd64.exe /quiet
}

Write-Output "Checking the Dependencies...."

pip install numpy
pip install pandas
pip install datetime
pip install matplotlib

Write-Output "Now, You are all set!"
