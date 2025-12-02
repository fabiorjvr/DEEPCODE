import sys
import subprocess
import json

checks = {
    "python_version": False,
    "git_installed": False,
    "deepcode_installed": False,
    "config_files_exist": False,
    "venv_active": False,
    "llm_configured": False
}

print("=" * 50)
print("  DeepCode - Verificador de Instalação")
print("=" * 50)
print()

# Check 1: Python version
print("[1/6] Verificando Python...")
py_version = sys.version_info
if py_version.major == 3 and py_version.minor >= 8:
    print(f"✅ Python {py_version.major}.{py_version.minor} OK")
    checks["python_version"] = True
else:
    print(f"❌ Python {py_version.major}.{py_version.minor} (mínimo 3.8)")

# Check 2: Git
print("\n[2/6] Verificando Git...")
try:
    subprocess.run(["git", "--version"], capture_output=True, check=True)
    print("✅ Git instalado")
    checks["git_installed"] = True
except:
    print("⚠️  Git não encontrado (opcional)")

# Check 3: DeepCode
print("\n[3/6] Verificando DeepCode...")
try:
    import deepcode
    print("✅ DeepCode importado com sucesso")
    checks["deepcode_installed"] = True
except ImportError as e:
    print(f"❌ Erro ao importar DeepCode: {e}")

# Check 4: Config files
print("\n[4/6] Verificando arquivos de configuração...")
import os
if os.path.exists("mcp_agent.secrets.yaml") and os.path.exists("mcp_agent.config.yaml"):
    print("✅ Arquivos de configuração encontrados")
    checks["config_files_exist"] = True

    # Verificar se API key está configurada
    with open("mcp_agent.secrets.yaml", "r") as f:
        content = f.read()
        if "api_key" in content and ("AIzaSy" in content or "gsk_" in content):
            print("✅ API key configurada")
            checks["llm_configured"] = True
        else:
            print("⚠️  API key não configurada (EDITE o arquivo!)")
else:
    print("❌ Arquivos de configuração não encontrados")

# Check 5: Virtual env
print("\n[5/6] Verificando ambiente virtual...")
in_venv = hasattr(sys, 'real_prefix') or (
    hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix
)
if in_venv:
    print("✅ Ambiente virtual ativado")
    checks["venv_active"] = True
else:
    print("⚠️  Não está em um ambiente virtual")

# Resumo
print("\n" + "=" * 50)
print("  RESUMO")
print("=" * 50)

passed = sum(checks.values())
total = len(checks)

for check, status in checks.items():
    symbol = "✅" if status else "❌"
    print(f"{symbol} {check.replace('_', ' ').title()}")

print(f"\nResultado: {passed}/{total} verificações passaram")

if passed == total:
    print("\n🎉 Instalação perfeita! Pronto para usar DeepCode!")
    print("Execute: deepcode")
elif passed >= 4:
    print("\n⚠️  Instalação funcional, mas configure API key!")
    print("Edite: mcp_agent.secrets.yaml")
else:
    print("\n❌ Problemas detectados. Reinstale seguindo o guia.")

sys.exit(0 if passed >= 4 else 1)