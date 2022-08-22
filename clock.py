from apscheduler.schedulers.blocking import BlockingScheduler
from app import main
from app import manda_mensagem

sched = BlockingScheduler()

# Iniciou Processo:
print("Running...")
manda_mensagem('New Deploy has Been Launched.')

# Colocando para Rodar a Função main a Cada 1s
sched.add_job(main, 'interval', seconds=1)
sched.start()