import datetime


def logger(func):
    def wrapped(time):
        with open('log_file.txt', 'a') as f:

            try:
                resulting = func(time)
                return resulting

            except TypeError:
                print([datetime.datetime.today().strftime("%d.%m.%Y %X"), 'TypeError'], file=f)

            except ValueError:
                print([datetime.datetime.today().strftime("%d.%m.%Y %X"), 'ValueError'], file=f)

            except ZeroDivisionError:
                print([datetime.datetime.today().strftime("%d.%m.%Y %X"), 'ZeroDivisionError'], file=f)

    return wrapped


@logger
def time_in_minutes(line):
    minutes = int(line[:2]) * 60 + int(line[3:5])
    return minutes


print(time_in_minutes('15:10'))
print(time_in_minutes('aa'))
print(time_in_minutes('0:07'))
