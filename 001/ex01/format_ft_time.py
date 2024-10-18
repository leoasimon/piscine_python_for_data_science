import time
test_epoch = 1666355857.3622

def format_number(number, decimal_places=4):
    return f"{number:,.{decimal_places}f}"

def format_scientific(number):
    return "{:.2e}".format(number)

def format_epoch_to_human(struct_time):
    return time.strftime("%b %d %Y", struct_time)

def main():
    current_epoch_time = time.time()
    formated = format_number(current_epoch_time)
    scientific = format_scientific(current_epoch_time)
    human_readable = format_epoch_to_human(time.localtime(current_epoch_time))

    print('Seconds since January 1, 1970: ' + formated + ' or ' + scientific +
          ' in scientific notation')
    print(human_readable)

if __name__ == '__main__':
    main()

