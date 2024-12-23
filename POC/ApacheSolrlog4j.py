
headers = {
    'User-Agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

def get_dnslog_domain():
    url = f'http://www.dnslog.cn/getdomain.php?t={random.random()}'
    r = requests.get(headers=headers ,url=url ,timeout=18)
    get_cookie = r.cookies.get_dict()
    for k ,v in get_cookie.items():
        cookie = f'{k}={v}'
    info = {'domain' :r.text ,'cookie' :cookie}
    return info

def get_dnslog_log(info):
    cookie = info['cookie']
    domain = info['domain']
    url = f'http://www.dnslog.cn/getrecords.php?t={random.random()}'
    headers.update({'Cookie' :cookie})
    r = requests.get(headers=headers ,url=url ,timeout=18)
    get_log_text = r.text
    if domain in get_log_text:
        return True
    else:
        return False

# 测试函数
if __name__ == "__main__":
    get_info = get_dnslog_domain()
    print(get_info)
    domain = get_info['domain']
    system(f'ping -c 1 {domain}')
    x = get_dnslog_log(get_info)
    print(x)