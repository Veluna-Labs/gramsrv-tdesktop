import re

for filename in ['canary-linux.yml', 'canary-windows.yml']:
    path = f'e:/100grm-ds/.github/workflows/{filename}'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the "Read canary configuration." step
    pattern = r"- name: Read canary configuration\.\s*shell: bash\s*run: \|\s*echo "CANARY_COUNTER=\$\{\{ needs\.version\.outputs\.counter \}\}" >> \.*?fi"
    
    replacement = """- name: Read canary configuration.
        shell: bash
        run: |
          echo "CANARY_COUNTER=\$\{\{ needs.version.outputs.counter \}\}" >> \
          echo "CANARY_SUFFIX=\$\{\{ needs.version.outputs.suffix \}\}" >> \
          echo "CANARY_VERSION=\$\{\{ needs.version.outputs.version_str \}\}" >> \
          echo "CANARY_FOLDER=\$\{\{ needs.version.outputs.folder \}\}" >> \
          echo "CANARY_KEY_ID=" >> \
          echo "CANARY_AZ_KEY=" >> \
          echo "CANARY_DEFINES=" >> \"""

    content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
