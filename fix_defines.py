import re

for filename in ['canary-linux.yml', 'canary-windows.yml']:
    path = f'e:/100grm-ds/.github/workflows/{filename}'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the complex CANARY_DEFINES assignment with an empty one
    content = re.sub(r'echo "CANARY_DEFINES=-D.*?" >> \$GITHUB_ENV', 'echo "CANARY_DEFINES=" >> $GITHUB_ENV', content)
    
    with open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(content)
