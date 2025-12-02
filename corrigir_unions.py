import re

def corrigir_union_types_completo(arquivo_path):
    """Corrige todos os Union types em um arquivo Python"""
    try:
        with open(arquivo_path, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Verificar se precisa de correção
        if " | " not in content:
            return False
            
        print(f"Corrigindo Union types em: {arquivo_path}")
        
        # Adicionar Union à importação se necessário
        if "from typing import" in content and "Union" not in content:
            content = content.replace(
                "from typing import",
                "from typing import Union,"
            )
        
        # Padrões para substituir
        substituicoes = [
            # Unions simples com None
            (r"str \| None", "Optional[str]"),
            (r"int \| None", "Optional[int]"),
            (r"bool \| None", "Optional[bool]"),
            (r"float \| None", "Optional[float]"),
            (r"dict\[str, Any\] \| None", "Optional[dict[str, Any]]"),
            (r"NotificationParams \| None", "Optional[NotificationParams]"),
            (r"RequestParams \| None", "Optional[RequestParams]"),
            
            # Unions complexos
            (r"Annotated\[int, Field\(strict=True\)\] \| str", "Union[Annotated[int, Field(strict=True)], str]"),
            (r"RequestParams \| dict\[str, Any\] \| None", "Union[RequestParams, dict[str, Any], None]"),
            (r"NotificationParams \| dict\[str, Any\] \| None", "Union[NotificationParams, dict[str, Any], None]"),
            (r"dict\[str, Any\] \| None", "Union[dict[str, Any], None]"),
            (r"Literal\[\"endTurn\", \"stopSequence\", \"maxTokens\", \"toolUse\"\] \| str", "Union[Literal[\"endTurn\", \"stopSequence\", \"maxTokens\", \"toolUse\"], str]"),
        ]
        
        # Aplicar substituições
        for padrao, substituto in substituicoes:
            content = re.sub(padrao, substituto, content)
        
        # Adicionar Optional à importação se usado
        if "Optional[" in content and "Optional" not in content:
            content = content.replace(
                "from typing import",
                "from typing import Optional,"
            )
        
        # Salvar arquivo
        with open(arquivo_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        return True
    except Exception as e:
        print(f"Erro ao corrigir {arquivo_path}: {e}")
        return False

# Corrigir o arquivo mcp/types.py
arquivo_mcp = r"C:\Users\FABIO\Desktop\PROJETOS\DEEPCODE\venv\Lib\site-packages\mcp\types.py"
if corrigir_union_types_completo(arquivo_mcp):
    print("✓ Arquivo mcp/types.py corrigido com sucesso!")
else:
    print("✗ Erro ao corrigir mcp/types.py")