import mcp.types
import inspect
from pydantic import BaseModel

print("Inspecting components of ElicitRequestParams...")
try:
    print(f"ElicitRequestURLParams base: {mcp.types.ElicitRequestURLParams.__bases__}")
    print(f"ElicitRequestFormParams base: {mcp.types.ElicitRequestFormParams.__bases__}")
except Exception as e:
    print(f"Error inspecting bases: {e}")

print(f"Is ElicitRequestParams a class? {isinstance(mcp.types.ElicitRequestParams, type)}")
print(f"Type of ElicitRequestParams: {type(mcp.types.ElicitRequestParams)}")
