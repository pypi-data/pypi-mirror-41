#!/bin/bash -eE
:<<"::batch"
@echo off
powershell -ExecutionPolicy ByPass -File .\scripts\test\test.ps1 %*
goto :end
::batch
test.sh $*
exit $?
:<<"::done"
:end
::done
exit