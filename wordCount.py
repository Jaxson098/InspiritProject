import sys

cantidates = ['biden', 'carter', 'clinton', 'dole', 'Hclinton', 'HWbush', 'mccain', 'obama','reagen','romney','trump','Wbush']
files = ['abortion.txt', 'crime.txt', 'defense spending.txt','education.txt', 'gun control.txt','gun violence.txt', 'healthcare.txt', 'immigration.txt', 'medicare.txt','millitary spending.txt','national security.txt']

count = 0

for can in cantidates:
    for file in files:
        path = f"./rawText/{can}/{file}"
        with open(path, 'r', encoding='utf-8') as toCount:
            text = toCount.read()
            words = text.split()
            count += len(words)
            print(count)

print(f"final: {count}")