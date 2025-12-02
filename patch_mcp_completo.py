import os
import glob

def corrigir_union_types(arquivo_path):
    """Corrige o uso de | para Union types em arquivos Python"""
    try:
        with open(arquivo_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Verificar se precisa de correção
        if " | " not in content:
            return False
            
        print(f"Corrigindo: {arquivo_path}")
        
        # Adicionar importações necessárias se não existirem
        if "from typing import" in content and "Union" not in content:
            content = content.replace(
                "from typing import",
                "from typing import Union, Optional,"
            )
        elif "from typing import" not in content and " | " in content:
            # Adicionar import no início
            lines = content.split('\n')
            insert_pos = 0
            for i, line in enumerate(lines):
                if line.strip() and not line.startswith('#') and not line.startswith('"""'):
                    insert_pos = i
                    break
            lines.insert(insert_pos, "from typing import Union, Optional")
            content = '\n'.join(lines)
        
        # Substituir unions simples
        content = content.replace("str | None", "Optional[str]")
        content = content.replace("int | None", "Optional[int]")
        content = content.replace("bool | None", "Optional[bool]")
        content = content.replace("float | None", "Optional[float]")
        
        # Substituir unions complexos
        content = content.replace("str | int", "Union[str, int]")
        content = content.replace("int | str", "Union[int, str]")
        
        # Salvar arquivo
        with open(arquivo_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        return True
    except Exception as e:
        print(f"Erro ao corrigir {arquivo_path}: {e}")
        return False

# Arquivos que precisam correção
arquivos_para_corrigir = [
    r"C:\Users\FABIO\Desktop\PROJETOS\DEEPCODE\venv\Lib\site-packages\mcp_agent\elicitation\types.py",
    r"C:\Users\FABIO\Desktop\PROJETOS\DEEPCODE\venv\Lib\site-packages\mcp\types.py"
]

for arquivo in arquivos_para_corrigir:
    if os.path.exists(arquivo):
        if corrigir_union_types(arquivo):
            print(f"✓ Corrigido: {arquivo}")
        else:
            print(f"- Sem alterações: {arquivo}")
    else:
        print(f"✗ Arquivo não encontrado: {arquivo}")

print("\nPatch completo aplicado!")