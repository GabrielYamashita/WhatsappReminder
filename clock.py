from apscheduler.schedulers.blocking import BlockingScheduler
from app import main

sched = BlockingScheduler()

# Marcando rodar a função a cada segundo
sched.add_job(main, 'interval', minutes=1)
sched.start()