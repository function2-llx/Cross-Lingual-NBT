import json

if __name__ == "__main__":
    with open('woz_tracking.json', 'r') as f:
        f = json.load(f)

    tot, hit = {}, {}
    slots = ["gegend", "essen", "request", "preisklasse"]
    for slot in slots:
        tot[slot] = hit[slot] = 0
    for dialog in f:
        for turn in dialog['dialogue']:
            pred_state = turn['Prediction']
            true_state = turn['True State']
            for slot in slots:
                true = true_state[slot]
                if true != 'none' and true != []:
                    tot[slot] += 1
                    if true == pred_state[slot]:
                        hit[slot] += 1

    for slot in slots:
        print('accuracy of {}: {}'.format(slot, hit[slot] / tot[slot]))
