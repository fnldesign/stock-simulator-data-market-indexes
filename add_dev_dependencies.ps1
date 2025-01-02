# Path to the .dev file
$devFile = ".\requirements.txt.dev"

# Check if the file exists
if (-Not (Test-Path $devFile)) {
    Write-Host "Error: File $devFile not found!" -ForegroundColor Red
    exit 1
}

# Read all lines from the .dev file
$dependencies = Get-Content $devFile

# Iterate over each dependency and add it to the Poetry dev group
foreach ($dependency in $dependencies) {
    if ($dependency -match "^\s*$") {
        continue  # Skip empty lines
    }
    Write-Host "Adding $dependency to the dev group..."
    try {
        poetry add --group dev $dependency
    } catch {
        Write-Host "Failed to add $dependency" -ForegroundColor Red
    }
}
