books = {'wdqk':['books.wdqkbook','WdqkBook']}

def gen_dbconf(mode):
    if mode == 'dev':
        return {'host':'localhost','db':'novel','user':'root','passwd':'912ZHEN'}
    else:
        return {'host':'127.6.123.1','db':'novel','user':'admin','passwd':'b4E3e3T8KRj8'}


