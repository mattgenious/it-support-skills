[CmdletBinding(SupportsShouldProcess)]
param([string]$Destination = (Join-Path $HOME '.config\opencode\skills'))
$ErrorActionPreference = 'Stop'
$source = Join-Path (Split-Path $PSScriptRoot -Parent) 'plugins\it-support\skills'
$skills = @(Get-ChildItem $source -Directory)
if ((Test-Path $Destination) -and (Get-Item $Destination).LinkType) { throw 'Destination must not be a link.' }
foreach ($skill in $skills) {
    $target = Join-Path $Destination $skill.Name
    if (Test-Path $target) { throw "Existing skill preserved: $target. Select another destination." }
}
if ($PSCmdlet.ShouldProcess($Destination, 'Install IT Support skill directories without overwriting existing skills')) {
    $null = New-Item -ItemType Directory -Path $Destination -Force
    foreach ($skill in $skills) { Copy-Item -LiteralPath $skill.FullName -Destination (Join-Path $Destination $skill.Name) -Recurse }
}
