import httpx
import sys

API_URL = "http://127.0.0.1:8000/openapi.json"
CLIENT_FILENAME = "client.py"

def generate_sdk():
    print(f"[*] Fetching OpenAPI schema from {API_URL}...")
    try:
        response = httpx.get(API_URL)
        response.raise_for_status()
        schema = response.json()
    except httpx.HTTPError as e:
        print(f"[!] Target API must be running. Failed to fetch schema: {e}")
        sys.exit(1)

    print("[*] Parsing paths and generating code...")
    
    code_lines = [
        '# AUTO-GENERATED CLIENT SDK',
        'import httpx',
        'from typing import Any, Dict, List',
        '\nclass ApiClient:',
        '    def __init__(self, base_url: str = "http://127.0.0.1:8000"):',
        '        self.base_url = base_url',
        '        self.client = httpx.Client(base_url=self.base_url)',
        '\n'
    ]

    paths = schema.get("paths", {})
    for path, methods in paths.items():
        for method, details in methods.items():
            operation_id = details.get("operationId", "unknown_operation")
            # Create a valid python method name
            method_name = operation_id.lower().replace("-", "_")
            
            # Simple parameter parsing
            args = ["self"]
            call_kwargs = {}
            path_params = []
            
            for param in details.get("parameters", []):
                if param["in"] == "path":
                    p_name = param["name"]
                    p_type = param["schema"].get("type", "Any")
                    # Naive mapping to python types
                    py_type = "int" if p_type == "integer" else "str"
                    args.append(f"{p_name}: {py_type}")
                    path_params.append(p_name)
                    
            route = path
            for p in path_params:
                # convert OpenAPI {id} to python f-string runtime vars
                pass
                
            has_body = "requestBody" in details
            if has_body:
                args.append("payload: Dict[str, Any]")
                call_kwargs["json"] = "payload"
                
            args_str = ", ".join(args)
            
            # Generate the method source code dynamically!
            code_lines.append(f'    def {method_name}({args_str}) -> Any:')
            code_lines.append(f'        """')
            code_lines.append(f'        {details.get("summary", "")}')
            code_lines.append(f'        Method: {method.upper()} | Route: {path}')
            code_lines.append(f'        """')
            
            formatted_path = f'f"{path}"' if "{" in path else f'"{path}"'
            
            request_args = [f'"{method.upper()}"', formatted_path]
            for k, v in call_kwargs.items():
                request_args.append(f'{k}={v}')
                
            request_str = ", ".join(request_args)
            
            code_lines.append(f'        response = self.client.request({request_str})')
            code_lines.append(f'        response.raise_for_status()')
            code_lines.append(f'        return response.json()')
            code_lines.append('\n')

    # Add a close method
    code_lines.extend([
        '    def close(self):',
        '        self.client.close()',
        '\n'
    ])
    
    # Write to file
    with open(CLIENT_FILENAME, "w", encoding="utf-8") as f:
        f.write("\n".join(code_lines))
        
    print(f"[+] Successfully generated Python SDK at {CLIENT_FILENAME}!")

if __name__ == "__main__":
    generate_sdk()
