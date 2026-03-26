"""Compile the .proto file into Python gRPC stubs."""
import subprocess
import sys


def generate():
    cmd = [
        sys.executable, "-m", "grpc_tools.protoc",
        "-I", "protos",
        "--python_out", ".",
        "--grpc_python_out", ".",
        "protos/product.proto",
    ]
    print("[*] Running protoc code generation...")
    result = subprocess.run(cmd, capture_output=True, text=True)

    if result.returncode == 0:
        print("[+] Generated: product_pb2.py, product_pb2_grpc.py")
    else:
        print(f"[!] Code generation failed:\n{result.stderr}")
        sys.exit(1)


if __name__ == "__main__":
    generate()
