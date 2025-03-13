# Requires running with administrative privileges

# Get all local user accounts
$localUsers = Get-LocalUser

# Create an empty array to store results
$results = @()

# Loop through each user
foreach ($user in $localUsers) {
    # Check if user is in Administrators group
    $isAdmin = $false
    try {
        $adminGroup = [ADSI]"WinNT://./Administrators,group"
        $members = @($adminGroup.Invoke("Members"))
        foreach ($member in $members) {
            $name = $member.GetType().InvokeMember("Name", 'GetProperty', $null, $member, $null)
            if ($name -eq $user.Name) {
                $isAdmin = $true
                break
            }
        }
    }
    catch {
        Write-Warning "Error checking admin status for $($user.Name): $_"
    }

    # Create custom object with user info
    $userInfo = [PSCustomObject]@{
        UserName       = $user.Name
        PermissionLevel = if ($isAdmin) { "Administrator" } else { "Standard User" }
        Enabled        = $user.Enabled
        LastLogon      = $user.LastLogon
        Description    = $user.Description
    }
    
    # Add to results array
    $results += $userInfo
}

# Display results in a formatted table
$results | Format-Table -AutoSize

# Optional: Export to CSV
# $results | Export-Csv -Path "LocalUserPermissions.csv" -NoTypeInformation
