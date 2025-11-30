# Test Groq-powered agent with 10 different queries
$endpoint = "https://web-production-4c3336.up.railway.app/api/sustainability-footprint-agent"

$queries = @(
    "What is carbon footprint?",
    "How can I reduce my energy consumption at home?",
    "Is driving 100 miles bad for the environment?",
    "What are the benefits of solar panels?",
    "How does recycling help the planet?",
    "Should I buy an electric car?",
    "What is the carbon footprint of eating meat?",
    "How can businesses reduce waste?",
    "What are green building certifications?",
    "Is air travel worse than driving for carbon emissions?"
)

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Testing Sustainability Agent with Groq" -ForegroundColor Cyan
Write-Host "========================================`n" -ForegroundColor Cyan

$i = 1
foreach ($query in $queries) {
    Write-Host "[$i/10] Query: $query" -ForegroundColor Yellow
    
    $body = @{
        messages = @(
            @{
                role = "user"
                content = $query
            }
        )
    } | ConvertTo-Json -Depth 10
    
    try {
        $response = Invoke-RestMethod -Uri $endpoint -Method Post -ContentType "application/json" -Body $body -ErrorAction Stop
        
        Write-Host "Status: $($response.status)" -ForegroundColor Green
        $message = $response.data.message
        if ($message.Length -gt 150) {
            Write-Host "Response: $($message.Substring(0, 150))..." -ForegroundColor White
        } else {
            Write-Host "Response: $message" -ForegroundColor White
        }
        Write-Host "Source: $($response.data.metadata.source)" -ForegroundColor Magenta
        
    } catch {
        Write-Host "Error: $_" -ForegroundColor Red
    }
    
    Write-Host "`n----------------------------------------`n"
    $i++
    Start-Sleep -Milliseconds 500
}

Write-Host "Test completed!" -ForegroundColor Cyan
