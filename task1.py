from datetime import datetime


def get_days_from_today(date):
    try:
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return None
    today = datetime.today().date()
    return (today - given_date).days


if __name__ == "__main__":
    print(get_days_from_today("2021-10-09"))
