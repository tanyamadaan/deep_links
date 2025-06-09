from qr_code_generator import generate_deep_link, generate_qr_code, bulk_read
import json
import sys
import os


try:
    print(sys.argv[1])
    print()
    for query_string in bulk_read(sys.argv[1]):
        deep_link = generate_deep_link(query_string)
        output_path = f"./qr_code_generator/output/{(query_string['context.bpp_id']).split('/')[0]}"
        if not os.path.isdir(output_path):
            os.mkdir(output_path)
        output_path = f"{output_path}/{query_string['message.intent.provider.id']}.png"
        generate_qr_code(deep_link, output_path)
except json.JSONDecodeError:
    print("Invalid JSON input.")
    raise
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    raise