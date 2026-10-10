dummy_version_job = '''  version:
    name: Version
    runs-on: depot-ubuntu-latest
    if: >-
      (github.event_name == 'push' || github.event_name == 'workflow_dispatch')
    outputs:
      channel: public
      chat_id: -1
      base: 7002009
      commit: $\{\{ github.sha \}\}
      counter: $\{\{ github.run_number \}\}
      previous: 0
      publish: false
      unsigned: true
      version_str: 7.2.9
      suffix: ''
      folder: 100Gramm
    steps:
      - run: echo "Dummy version job"
'''

for filename in ['canary-linux.yml', 'canary-windows.yml']:
    path = f'e:/100grm-ds/.github/workflows/{filename}'
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    start_idx = -1
    end_idx = -1
    for i, line in enumerate(lines):
        if line.startswith('  version:'):
            start_idx = i
            break
            
    if start_idx != -1:
        for i in range(start_idx + 1, len(lines)):
            if lines[i].startswith('  ') and not lines[i].startswith('    ') and lines[i].strip() != '':
                end_idx = i
                break
        
        if end_idx == -1: end_idx = len(lines)
        
        # Replace
        new_lines = lines[:start_idx] + [dummy_version_job.replace('$', '$').replace('\{', '{').replace('\}', '}') + '\n'] + lines[end_idx:]
        
        with open(path, 'w', encoding='utf-8', newline='') as f:
            f.writelines(new_lines)
