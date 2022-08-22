from apscheduler.schedulers.blocking import BlockingScheduler
from app import main
from app import deploy_check

sched = BlockingScheduler()

# Iniciou Processo:
print("Running...")
deploy_check()

# Marcando rodar a função a cada segundo
sched.add_job(main, 'interval', seconds=1)
sched.start()