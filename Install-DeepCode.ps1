# Script: Install-DeepCode.ps1

param(
    [string]$InstallPath = "$env:USERPROFILE\DeepCode_Workspace",
    [string]$PythonVersion = "3.11"
)

$ErrorActionPreference = "Stop"

Write-Host "╔════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║  DeepCode - Instalador PowerShell v1  ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Função para verificar comando
function Test-Command {
    param([string]$Command)
    try {
        if (Get-Command $Command -ErrorAction Stop) {
            return $true
        }
    }
    catch {
        return $false
    }
}

# PASSO 1: Verificar Python
Write-Host "[1/7] Verificando Python..." -ForegroundColor Yellow

if (-not (Test-Command python)) {
    Write-Host "❌ Python não encontrado!" -ForegroundColor Red
    Write-Host "Baixe em: https://www.python.org/downloads/" -ForegroundColor Red
    Read-Host "Pressione Enter para sair"
    exit 1
}

$pythonVer = python --version 2>&1
Write-Host "✅ $pythonVer encontrado" -ForegroundColor Green

# PASSO 2: Verificar Git
Write-Host "`n[2/7] Verificando Git..." -ForegroundColor Yellow

if (Test-Command git) {
    $gitVer = git --version
    Write-Host "✅ $gitVer encontrado" -ForegroundColor Green
} else {
    Write-Host "⚠️  Git não encontrado (opcional)" -ForegroundColor Yellow
}

# PASSO 3: Criar diretório
Write-Host "`n[3/7] Criando diretório de trabalho..." -ForegroundColor Yellow

if (-not (Test-Path $InstallPath)) {
    New-Item -ItemType Directory -Path $InstallPath | Out-Null
    Write-Host "✅ Diretório criado: $InstallPath" -ForegroundColor Green
} else {
    Write-Host "✅ Diretório já existe: $InstallPath" -ForegroundColor Green
}

Set-Location -Path $InstallPath

# PASSO 4: Criar ambiente virtual
Write-Host "`n[4/7] Criando ambiente virtual..." -ForegroundColor Yellow

if (-not (Test-Path "venv")) {
    python -m venv venv
    Write-Host "✅ Ambiente virtual criado" -ForegroundColor Green
} else {
    Write-Host "✅ Ambiente virtual já existe" -ForegroundColor Green
}

# PASSO 5: Ativar venv e instalar
Write-Host "`n[5/7] Ativando ambiente virtual..." -ForegroundColor Yellow
& .\venv\Scripts\Activate.ps1
Write-Host "✅ Ambiente virtual ativado" -ForegroundColor Green

# PASSO 6: Atualizar pip e instalar
Write-Host "`n[6/7] Instalando DeepCode (pode levar 2-3 minutos)..." -ForegroundColor Yellow
python -m pip install --upgrade pip -q
pip install deepcode-hku -q

Write-Host "✅ DeepCode instalado" -ForegroundColor Green

# PASSO 7: Baixar configs
Write-Host "`n[7/7] Baixando arquivos de configuração..." -ForegroundColor Yellow

$urls = @{
    "mcp_agent.secrets.yaml" = "https://raw.githubusercontent.com/HKUDS/DeepCode/main/mcp_agent.secrets.yaml"
    "mcp_agent.config.yaml" = "https://raw.githubusercontent.com/HKUDS/DeepCode/main/mcp_agent.config.yaml"
}

foreach ($file in $urls.Keys) {
    if (-not (Test-Path $file)) {
        try {
            Invoke-WebRequest -Uri $urls[$file] -OutFile $file -ErrorAction Stop
            Write-Host "✅ $file baixado" -ForegroundColor Green
        }
        catch {
            Write-Host "⚠️  Erro ao baixar $file" -ForegroundColor Yellow
            New-Item -ItemType File -Name $file | Out-Null
        }
    } else {
        Write-Host "✅ $file já existe" -ForegroundColor Green
    }
}

# CONCLUSÃO
Write-Host "`n╔════════════════════════════════════════╗" -ForegroundColor Green
Write-Host "║  ✅ INSTALAÇÃO CONCLUÍDA!              ║" -ForegroundColor Green
Write-Host "╚════════════════════════════════════════╝" -ForegroundColor Green

Write-Host "`nℹ️  Informações importantes:" -ForegroundColor Cyan
Write-Host "📁 Diretório: $InstallPath"
Write-Host "🐍 Python: $pythonVer"
Write-Host ""
Write-Host "🔑 PRÓXIMO PASSO: Configure sua API key" -ForegroundColor Yellow
Write-Host "   Edite: $InstallPath\mcp_agent.secrets.yaml" -ForegroundColor Yellow
Write-Host ""
Write-Host "🚀 Para iniciar DeepCode:" -ForegroundColor Cyan
Write-Host "   deepcode" -ForegroundColor Green
Write-Host ""
Write-Host "🌐 Abrirá em: http://localhost:8501" -ForegroundColor Cyan

Read-Host "`nPressione Enter para finalizar"
