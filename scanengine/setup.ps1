.\clamd.exe --install-service 
.\freshclam.exe --install-service
set-service -Name clamd -StartupType Automatic
set-service -Name freshclam -StartupType Automatic
Set-Service -name clamd -DisplayName "Brienprotect real-time protection"
Set-Service -name clamd -description "Provides virus scanning facilities for brienprotect"
Set-Service -name freshclam -DisplayName "Brienprotect update"
Set-Service -name freshclam -description "Updates virus pattern database for brienprotect"