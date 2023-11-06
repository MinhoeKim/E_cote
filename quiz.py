def solution(fees, records):
    print(fees)
    print(records)
    copy_records = []
    for record in records:
        time_str,number,check = record.split(' ')
        hour, minute = int(time_str[:2]), int(time_str[3:])
        time = hour*60 + minute
        copy_records.append([time,number,check])

    parking_cars = []
    time_and_numbers = []
 
    for copy_record in copy_records:
        if copy_record[2] == 'IN':
            parking_cars.append(copy_record)
        if copy_record[2] == 'OUT':
            for i in range(len(parking_cars)):
                if parking_cars[i][1] == copy_record[1] and parking_cars[i][2] == 'IN':

                    parking_time = copy_record[0] - parking_cars[i][0]

                    time_and_numbers.append([parking_time, parking_cars[i][1]])
                    parking_cars[i][2] = '처리완료'

    for i in range(len(parking_cars)):
        if parking_cars[i][2] == "IN":
            parking_time = (23*60+59) - parking_cars[i][0]
            time_and_numbers.append([parking_time, parking_cars[i][1]])
            parking_cars[i][2] = '처리완료'

    print('타임앤넘버', time_and_numbers)
    numbers = []
    for a,b in time_and_numbers:
        numbers.append(b)
    numbers = set(numbers)
    numbers = list(numbers)
    print(numbers)
    sum_time_and_number = []
    for number in numbers:
        time = 0
        for a,b in time_and_numbers:
            if number == b:
                time += a
        sum_time_and_number.append([time,number])
    print('')
    print(sum_time_and_number)

    fees_numbers = []
    for time, number in sum_time_and_number:
        fee = 0
        if time <= fees[0]:
            fee += fees[1]
            fees_numbers.append([fee,number])
        else:
            time -= fees[0]
            fee += fees[1]
            fee += (time//fees[2])*fees[3]
            if time%fees[2] > 0 :
                fee += fees[3]
            fees_numbers.append([fee,number])
    fees_numbers.sort(key = lambda x : x[1])
    print('마지막',fees_numbers)
    answer = []
    for a,b in fees_numbers:
        answer.append(a)
    return answer