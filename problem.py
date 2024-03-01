def findingUsersActiveMinutes(logs, k):
    result = []
    uam_log = {}

    for i in logs:
        if i[0] not in uam_log.keys():
            uam_log[i[0]] = [i[1]]
        else:
            if i[1] not in uam_log[i[0]]:
                uam_log[i[0]] += [i[1]]

    for i in range(k):
        result.append(0)

    for i in uam_log.values():
        result[len(i) - 1] += 1

    return print(result)


findingUsersActiveMinutes([[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]], 5)
