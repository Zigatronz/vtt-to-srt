
import os

print('Input vtt to convert to srt:')
vtt = input(' > ')
if not os.path.exists(vtt):
    print('File not exist.')
    exit()
if not vtt.endswith('.vtt'):
    print('Wrong file format.')
    exit()

srt = vtt.removesuffix('.vtt') + '.srt'

if os.path.exists(srt):
    print('SRT file detected. Remove it before proceed.')
    exit()

index = 0
with open(vtt, 'r') as file:
    data = file.read()
    outputData = ''
    for line in data.split('\n'):
        if ' --> ' in line:
            index += 1
            newLine = str(index) + '\n' + line.replace('.', ',')
        else:
            newLine = line
        outputData = outputData + newLine + '\n'
    with open(srt, 'x') as srt_file:
        srt_file.write(outputData)

print('Done.')
