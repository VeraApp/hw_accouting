from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
import rich




if __name__ == '__main__':
    print(f"Сегодня: {datetime.now().date()}")
    calculate_salary()
    get_employees()
