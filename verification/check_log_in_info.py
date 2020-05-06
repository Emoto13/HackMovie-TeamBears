from gateway.gateway_check_log_in_info import check_log_in_info_gateway


def check_log_in_info(login_info):
    info = check_log_in_info_gateway(login_info)
    if len(info) == 0:
        raise ValueError('Wrong user name or password')
