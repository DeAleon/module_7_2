def custom_write(file_name, strings):
    count = 0
    bait = {}
    for i in strings:
        file = open(file_name, 'a', encoding='utf-8')
        count += 1
        bait[count, file.tell()] = i
        file.write(f'{i}\n')
        file.close()
    return bait


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
