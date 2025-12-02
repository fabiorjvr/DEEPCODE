import mcp.types
import inspect

print("Attributes in mcp.types:")
for name in dir(mcp.types):
    if "Elicit" in name:
        print(f"Found: {name}")

try:
    from mcp.types import ElicitRequestParams
    print("Successfully imported ElicitRequestParams")
    print(inspect.signature(ElicitRequestParams))
except ImportError as e:
    print(f"ImportError: {e}")
except Exception as e:
    print(f"Error: {e}")
