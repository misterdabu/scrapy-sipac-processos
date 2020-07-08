from flask_script import Manager
from flask import Flask
from app.main.controller.processos_controller import app
from app.main.service.processos_service import ProcessoService
from apscheduler.schedulers.background import BackgroundScheduler
from app.main.bd.repository import init_bd

service = ProcessoService()

cron = BackgroundScheduler(daemon=True, timezone='America/Sao_Paulo')
cron.add_job(service.update_processos, 'cron', day="1-16", day_of_week=(
    'mon-fri'), hour='7-16')

app.app_context().push()

manager = Manager(app)


@manager.command
def run():
    init_bd()
    cron.start()
    app.run()

manager.run()