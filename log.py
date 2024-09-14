import logging
from logging import handlers

class Logger(object):

  # 日志级别关系映射

  level_relations = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'crit': logging.CRITICAL
  }

  def __init__(self,
               filename,
               level: str = 'info',
               when='D',
               back_count=3,
               fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
    self.logger = logging.getLogger(filename)
    format_str = logging.Formatter(fmt)
    self.logger.setLevel(self.level_relations.get(level))
    sh = logging.StreamHandler()
    sh.setFormatter(format_str)
    th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=back_count, encoding='UTF-8')
    th.setFormatter(format_str)
    self.logger.addHandler(sh)
    self.logger.addHandler(th)
