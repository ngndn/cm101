__author__ = 'nadan'

import csv


def pre_process():
    scores = dict()
    with open('/home/nadan/class.csv', 'r') as f:
        students = csv.DictReader(f, delimiter=',', quotechar='"')
        for student in students:
            scores[student['Student ID']] = {
                'self': 0,
                'group': 0,
                'peer': []
            }
    return scores


def get_score():

    scores = pre_process()
    with open('/home/nadan/PeerEval.csv', 'r') as f:
        evaluations = csv.DictReader(f, delimiter=',', quotechar='"')
        for evaluate in evaluations:
            scores[evaluate['aid']]['self'] = int(evaluate['aeval'])
            scores[evaluate['aid']]['group'] = float(evaluate['geval'])
            for key in ['p1', 'p2', 'p3', 'p4']:
                if evaluate[key + 'id'] in scores:
                    scores[evaluate[key + 'id']]['peer'].append(int(evaluate[key + 'eval']))

    return scores


def to_scv(scores):
    with open('/home/nadan/peer.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(['ID', 'Self', 'Peer', 'AvgPeer', 'Group'])
        for key, value in scores.items():
            if len(value['peer']) != 0:
                avg_peer = sum(value['peer']) / len(value['peer'])
            else:
                avg_peer = 0
            writer.writerow([key, str(value['self']), str(value['peer']), str(avg_peer), str(value['group'])])

to_scv(get_score())