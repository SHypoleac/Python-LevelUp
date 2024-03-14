from apscheduler.schedulers.blocking import BlockingScheduler

print("Hello, use Schedule(function,hour,minute) to send your function into the future")

def exe():
    exec(open("/home/mich/Dokumenty/Projekty/MenadżerPracy/KalendarzPracy.py").read())

def Schedule(function,h,m):
    scheduler = BlockingScheduler()
    scheduler.add_job(function, 'cron', hour=h, minute=m)
    scheduler.start()
