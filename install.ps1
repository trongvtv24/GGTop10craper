<#
.SYNOPSIS
    Cài đặt Research SEO Skill cho Antigravity Workflow Framework (AWF).
    - Sao chép thư mục gốc vào `~/.gemini/antigravity/skills/`
    - Đặt lệnh `/Research SEO` vào `~/.gemini/antigravity/global_workflows/`
#>

$AWF_DIR = "$HOME\.gemini\antigravity"
$SKILLS_DIR = "$AWF_DIR\skills"
$WORKFLOW_DIR = "$AWF_DIR\global_workflows"

$SKILL_NAME = "research-seo-skill"
$WORKFLOW_FILE = "research_seo.md"

# 1. Kiểm tra tồn tại thư mục AWF
if (!(Test-Path -Path $AWF_DIR)) {
    Write-Host "❌ Lỗi: Không tìm thấy thư mục Antigravity tại $AWF_DIR." -ForegroundColor Red
    Write-Host "Vui lòng cài đặt Antigravity trước!" -ForegroundColor Yellow
    exit
}

# 2. Tạo folders nếu chưa có
if (!(Test-Path -Path $SKILLS_DIR)) {
    New-Item -ItemType Directory -Force -Path $SKILLS_DIR | Out-Null
    Write-Host "Kích hoạt tạo folder skills..."
}
if (!(Test-Path -Path $WORKFLOW_DIR)) {
    New-Item -ItemType Directory -Force -Path $WORKFLOW_DIR | Out-Null
    Write-Host "Kích hoạt tạo folder workflows..."
}

# 3. Chép toàn bộ thư mục gốc vào Skills (ẩn thư mục .git, venv)
Write-Host "🔄 Đang sao chép mã nguồn Skill..." -ForegroundColor Cyan
$DEST_SKILL = "$SKILLS_DIR\$SKILL_NAME"
# Robocopy để sao chép nâng cao (bỏ qua git, venv, pycache, configs)
robocopy ".\ " $DEST_SKILL /E /XD ".git" "venv" "__pycache__" "configs" /NJH /NJS /NDL /NC /NS

if ($LASTEXITCODE -lt 8) {
    Write-Host "✅ Đã cài đặt Skill vào: $DEST_SKILL" -ForegroundColor Green
} else {
    Write-Host "❌ Sao chép Skill thất bại!" -ForegroundColor Red
    exit
}

# 4. Chép file Workflow vào Global Workflows
Write-Host "🔄 Đang đăng ký Lệnh /Research SEO..." -ForegroundColor Cyan
Copy-Item ".\workflow\$WORKFLOW_FILE" -Destination "$WORKFLOW_DIR\$WORKFLOW_FILE" -Force
Write-Host "✅ Đã cài đặt Lệnh vào: $WORKFLOW_DIR\$WORKFLOW_FILE" -ForegroundColor Green

# 5. Hoàn tất
Write-Host "`n🎉 CÀI ĐẶT HOÀN TẤT!" -ForegroundColor Green
Write-Host "Bây giờ bạn có thể chat với Antigravity và gõ: /Research SEO [từ_khóa] để trải nghiệm.`n" -ForegroundColor Yellow
