
for line in dataset_file:
    line = line.lower().split()
    for i, word in enumerate(line):
        if i == len(line)-1:
            model['END'] = model.get('END', []) + [word]
        else:
            if i == 0:
                model['START'] = model.get('START', []) + [word]
            model[word] = model.get(word, []) + [line[i+1]]