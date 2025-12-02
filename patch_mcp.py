import os

file_path = r"C:\Users\FABIO\DeepCode_Workspace\venv\Lib\site-packages\mcp_agent\elicitation\types.py"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

new_content = content.replace("from typing import Protocol", "from typing import Protocol, Union")
new_content = new_content.replace("server_name: str | None = None", "server_name: Union[str, None] = None")
new_content = new_content.replace("-> ElicitResult | ErrorData:", "-> Union[ElicitResult, ErrorData]:")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Patch applied successfully.")
