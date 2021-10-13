from apscheduler.schedulers.blocking import BlockingScheduler
from app import main

sched = BlockingScheduler()

# Iniciou Processo:
print("Running...")

# Marcando rodar a função a cada segundo
sched.add_job(main, 'interval', seconds=1)
sched.start()