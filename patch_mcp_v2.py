import os

# Atualizar para o novo caminho do venv
file_path = r"C:\Users\FABIO\Desktop\PROJETOS\DEEPCODE\venv\Lib\site-packages\mcp_agent\elicitation\types.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Corrigir a importação e o uso de Union types para Python 3.13
new_content = content.replace(
    "from typing import Protocol",
    "from typing import Protocol, Union, Optional"
)

# Substituir o uso de | por Union para compatibilidade
new_content = new_content.replace(
    "server_name: str | None = None",
    "server_name: Optional[str] = None"
)

# Também corrigir o retorno da função
new_content = new_content.replace(
    "ElicitResult | ErrorData",
    "Union[ElicitResult, ErrorData]"
)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Patch v2 aplicado com sucesso - compatibilidade Python 3.13 restaurada.")
