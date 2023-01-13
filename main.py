def Av_Points():
    journal = {}
    for i in range(int(input("Введите количество записей: "))):
        name, subject, appraisal = input("Фамилия, предмет, оценка: ").split()
        if subject in journal:
            journal[subject].append(int(appraisal))
        else:
            journal[subject] = [int(appraisal)]

    for subject, appraisals in journal.items():
        print("%s %.1f" % (subject, sum(appraisals) / len(appraisals)))
    Av_Points()

    print("%s %.1f" % (subject, sum(appraisals) / len(appraisals)))
    return Av_Points()