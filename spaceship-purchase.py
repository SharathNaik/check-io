# http://www.checkio.org/mission/task/info/spaceship-purchase/python-27/

def checkio(offers):
    '''
    the amount of money that Petr will pay for the ride
    '''
    initial_petr, raise_petr, initial_driver,
    reduction_driver = offers
    min_driver = initial_driver - reduction_driver
    return min_driver / 2

if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450, 'First'
    assert checkio([150, 50, 900, 100]) == 400, 'Second'
    print 'All is ok'
