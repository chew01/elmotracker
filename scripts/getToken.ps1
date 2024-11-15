# Define the path to the log file
$logFilePath = "$env:USERPROFILE\AppData\LocalLow\SunBorn\EXILIUM\Player.log"

# Define the regex pattern to extract xindong_uid and access_token
$regexPattern = '"xindong_uid":(\d+).+"access_token":"(.+?)"'

# Check if the log file exists
if (Test-Path $logFilePath) {
    # Read the content of the log file
    $logContent = Get-Content -Path $logFilePath -Raw

    # Match the regex pattern
    $matches = [regex]::Matches($logContent, $regexPattern)

    if ($matches.Count -gt 0) {
        # Get the last match
        $lastMatch = $matches[$matches.Count - 1]

        # Extract the values
        $xindongUid = $lastMatch.Groups[1].Value
        $accessToken = $lastMatch.Groups[2].Value

        # Copy the results
        $historyToken = "$xindongUid@$accessToken"

        Write-Host $historyToken
        Set-Clipboard -Value $historyToken
        Write-Host "Link copied to clipboard" -ForegroundColor Green
    } else {
        Write-Output "No matches found."
    }
} else {
    Write-Output "Log file not found at path: $logFilePath"
}
