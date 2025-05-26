# ~/frappe-bench/apps/rnd_nutrition/rnd_nutrition/tasks.py
from frappe.utils.background_jobs import scheduler

def daily():
    """Example daily task"""
    pass

def hourly():
    """Example hourly task"""
    pass

def all():
    return {
        'daily': {
            'task': 'rnd_nutrition.tasks.daily',
            'frequency': 'daily'
        }
    }
