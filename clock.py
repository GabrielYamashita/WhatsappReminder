from apscheduler.schedulers.blocking import BlockingScheduler
from app import main
from app import manda_mensagem

sched = BlockingScheduler()

# Iniciou Processo:
print("Running...")
manda_mensagem('New Deploy has Been Launched.')

# Marcando rodar a função a cada segundo
sched.add_job(main, 'interval', seconds=1)
sched.start()