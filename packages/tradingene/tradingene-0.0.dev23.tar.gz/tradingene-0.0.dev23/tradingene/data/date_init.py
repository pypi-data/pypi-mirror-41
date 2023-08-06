from datetime import datetime, timedelta
from tradingene.algorithm_backtest import limits
import tradingene.data.weekends as weekends

def date_init(alg):
    instr_list = list(alg.instruments)
    timeframes = {instr.timeframe for instr in instr_list}
    ticker = instr_list[0].ticker
    pre_start_date = start_date = alg.start_date
    end_date = alg.end_date
    if ticker not in limits.moex_tickers:
        pre_start_date = calculate_crypto_dates(instr_list, start_date)
    else:
        start_date = _moex_start_date(start_date)
        pre_start_date = _moex_pre_start_date(start_date, max(timeframes))
        end_date = _moex_end_date(end_date)
    return pre_start_date, start_date, end_date


def calculate_crypto_dates(instruments, start_date):
    lookback = limits.LOOKBACK_PERIOD
    earliest_start = limits.EARLISET_START
    timeframe = max({instr.timeframe for instr in instruments})
    pre_start_date = \
                start_date -  timedelta(minutes = lookback * timeframe)
    if pre_start_date < earliest_start:
        pre_start_date = earliest_start
    return pre_start_date


def _moex_start_date(start_date):
    if start_date.weekday() == 5:
        start_date += timedelta(days=2)
    elif start_date.weekday() == 6:
        start_date += timedelta(days=1)
    if start_date.hour < 7:
        new_hour = 7
        new_minute = 0
        new_second = 0
    elif start_date.hour >= 20 and start_date.minutes > 49:
        start_date += timedelta(days=1)
        new_hour = 7
        new_minute = 0
        new_second = 0
    else:
        new_hour = start_date.hour
        new_minute = start_date.minute
        new_second = start_date.second
    candidate_date = datetime(
        start_date.year,
        start_date.month,
        start_date.day)
    while candidate_date in weekends.days_off:
        candidate_date += timedelta(days=1)
    new_start_date = datetime(
        candidate_date.year, 
        candidate_date.month,
        candidate_date.day,
        new_hour,
        new_minute,
        new_second
        )
    return new_start_date


def _moex_pre_start_date(moex_start_date, max_timeframe):
    pre_start_date = moex_start_date
    evening_sesson = 285
    day_session = 700
    day_minutes = day_session + evening_sesson
    days = max_timeframe*50//day_minutes + 1
    i = days
    while i > 0:
        foo = pre_start_date - timedelta(days=1)
        candidate = datetime(
            foo.year,
            foo.month,
            foo.day
        )
        if candidate.weekday() not in (5,6) and candidate not in weekends.days_off:
            i -= 1
        pre_start_date = candidate
    moex_pre_start_date = datetime(
        pre_start_date.year,
        pre_start_date.month,
        pre_start_date.day,
        7
    )
    return moex_pre_start_date

    
def _moex_end_date(end_date):
    if end_date.weekday() == 5:
        end_date += timedelta(days=2)
    elif end_date.weekday() == 6:
        end_date += timedelta(days=1)
    if end_date.hour < 7:
        end_date -= timedelta(days=1)
        new_hour = 20
        new_minute = 49
        new_second = 0
    elif start_date.hour >= 20 and start_date.minutes > 49:
        new_hour = 20
        new_minute = 49
        new_second = 0
    else:
        new_hour = end_date.hour
        new_minute = end_date.minute
        new_second = end_date.second
    candidate_date = datetime(
        end_date.year,
        end_date.month,
        end_date.day)
    while candidate_date in weekends.days_off or candidate_date.weekday() in (5,6):
        candidate_date += timedelta(days=1)
    new_end_date = datetime(
        candidate_date.year, 
        candidate_date.month,
        candidate_date.day,
        new_hour,
        new_minute,
        new_second
        )
    return new_end_date