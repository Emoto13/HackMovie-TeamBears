from templates.templates_log_in import get_login_info
from verification.verification_check_log_in_info import check_log_in_info
from decorators.decorators_log_in import check_if_logged_in


@check_if_logged_in
def log_in(factory):
    name, password = get_login_info()
    check_log_in_info([name, password])
    factory.user_name = name
    factory.is_logged_in = True
