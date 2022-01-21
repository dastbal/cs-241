
def info_commercial_rate_by_type(data, type):
    index = 0
    comm_rates = []
    for i in range(1, len(data)):
        comm_rate = data[i].split(',')[6]
        comm_rates.append(comm_rate)

    if type == 'min':
        index = comm_rates.index(min(comm_rates))

    if type == 'max':
        index = comm_rates.index(max(comm_rates))

    return data[index + 1].split(',')


def sum_rates(list):
    sum = 0
    for rate in list:
        sum = sum + float(rate)
    return sum


def average_comm_rate(data):
    comm_rates = []
    for i in range(1, len(data)):
        comm_rate = data[i].split(',')[6]
        comm_rates.append(comm_rate)
    average = sum_rates(comm_rates) / (len(comm_rates))
    return average


def main():
    name_of_file = input('Please enter the data file: ')
    file = open(name_of_file, 'r')
    average = average_comm_rate(file.readlines())
    file = open(name_of_file, 'r')
    highest = info_commercial_rate_by_type(file.readlines(), 'max')
    file = open(name_of_file, 'r')
    lowest = info_commercial_rate_by_type(file.readlines(), 'min')

    print()
    print(f'The average commercial rate is: {average}')
    print()
    print(
        f'The highest rate is:\n{highest[2]} ({highest[0]}, {highest[3]}) - ${highest[6]}')
    print()
    print(
        f'The lowest rate is:\n{lowest[2]} ({lowest[0]}, {lowest[3]}) - ${float(lowest[6])}')


main()
