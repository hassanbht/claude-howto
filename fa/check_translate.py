import os

zh_dir = 'D:/Project/claude-howto/zh'
fa_dir = 'D:/Project/claude-howto/fa'

zh_files = []
for root, dirs, files in os.walk(zh_dir):
    for f in files:
        if f.endswith('.md'):
            zh_files.append(os.path.join(root, f))

fa_files = []
for root, dirs, files in os.walk(fa_dir):
    for f in files:
        if f.endswith('.md'):
            fa_files.append(os.path.join(root, f))

zh_rel = set()
for f in zh_files:
    zh_rel.add(f.replace(zh_dir + '/', ''))

fa_abs = set()
for f in fa_files:
    fa_abs.add(f)

left = []
for rel in sorted(zh_rel):
    fa_path = fa_dir + '/' + rel
    if not os.path.exists(fa_path):
        left.append(rel)

print('Total zh markdown files:', len(zh_rel))
print('Total fa markdown files:', len(fa_abs))
print('Remaining to translate:', len(left))
for f in left:
    print('  -', f)
