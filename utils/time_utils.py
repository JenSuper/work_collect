from datetime import datetime
import logging

fmt_time = '%Y-%m-%d %H:%M:%S'
fmt_time_hm = '%H:%M'
fmt_date_time_hm = '%Y-%m-%d %H:%M'

# strptime()：它是将字符串解析为 datetime 对象的方法
# strftime()：它是将 datetime 对象转换为指定格式的字符串的方法


# 时间戳转换为字符串时间
def convert_timestamp_to_str(content):
    return datetime.fromtimestamp(int(content)).strftime(fmt_time)


# 时间戳(毫秒)转换为时间
def convert_timestamp_to_datetime(content):
    return datetime.fromtimestamp(float(content) / 1000)

#  时间戳转换为 datetime ， str
def str_to_datetime(content):
    # str to datetime
    timestamp = convert_timestamp_to_datetime(content)
    # datetime to str
    time_str = convert_datetime_to_str(timestamp)
    # str to datetime
    datetime = convert_str_to_datetime(time_str)
    return datetime,time_str


# 当前时间转为字符串
def curr_time_str():
    return datetime.now().strftime(fmt_time)

def custom_datetime():
    return convert_str_to_datetime('2023-06-05 13:30:00')

def curr_datetime_str():
    return datetime.strftime(datetime.now(), fmt_time)

# 当前时间
def curr_datetime():
    return datetime.now()


# str -> datetime
def convert_str_to_datetime(content):
    return datetime.strptime(content, fmt_time)

# datetime -> str
def convert_datetime_to_str(content):
    return datetime.strftime(content, fmt_time)

# 当前时间在凌晨12点到上午7点之间，不发消息
def check_pull_data():
    cur_time = datetime.now()
    hour = cur_time.hour
    if 0 < hour < 7:
        logging.info("当前时间为：%d,暂停数据拉取", hour)
        return True
    return False


def time_now_hm():
    return datetime.now().strftime(fmt_date_time_hm)


def time_now_hm_diff(time1_str, time2_str):
    time1 = datetime.strptime(time1_str, fmt_date_time_hm)
    time2 = datetime.strptime(time2_str, fmt_date_time_hm)
    if time1 > time2:
        return True, time1_str, ">"
    if time1 == time2:
        return True, time1_str, "="
    return False, time1_str, ""

if __name__ == '__main__':
    print(time_now_hm_diff('2024-06-21 23:40','2024-06-22 00:01'))
    # print(time_now_hm())
