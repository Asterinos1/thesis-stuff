$scriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
$repoRoot = (Resolve-Path "$scriptDir\..").Path
$files = Get-ChildItem -Path $repoRoot -Filter *.tex -Recurse
$lastWriteTimes = @{}

foreach ($file in $files) {
    $lastWriteTimes[$file.FullName] = $file.LastWriteTime
}

Write-Host "Watching for changes in .tex files..."
Write-Host "Press Ctrl+C to stop this script if running manually."

while ($true) {
    $files = Get-ChildItem -Path $repoRoot -Filter *.tex -Recurse
    $changed = $false
    
    foreach ($file in $files) {
        if (-not $lastWriteTimes.ContainsKey($file.FullName) -or $lastWriteTimes[$file.FullName] -ne $file.LastWriteTime) {
            Write-Host "`n[$((Get-Date).ToString('HH:mm:ss'))] Detected change in $($file.Name). Recompiling..."
            $lastWriteTimes[$file.FullName] = $file.LastWriteTime
            $changed = $true
        }
    }
    
    if ($changed) {
        # Run pdflatex (once for speed). The user can still run build.bat if citations change.
        $process = Start-Process pdflatex -ArgumentList "-interaction=nonstopmode", "main.tex" -WorkingDirectory $scriptDir -NoNewWindow -Wait -PassThru
        
        if ($process.ExitCode -eq 0) {
            Write-Host "Successfully compiled main.pdf!" -ForegroundColor Green
        } else {
            Write-Host "Compilation failed. Check the errors in your LaTeX file." -ForegroundColor Red
        }
    }
    
    Start-Sleep -Seconds 2
}
