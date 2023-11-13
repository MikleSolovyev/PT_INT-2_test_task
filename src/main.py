import json
import logging.config

from pydantic import ValidationError

from config import Config
from db import Database
from host import Host
from ssh import SSHClient

CONFIG_PATH = 'config/config.yaml'

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # parse config
    cfg = Config.load(CONFIG_PATH)

    # setup logger
    logging.config.dictConfig(cfg.logger)
    logger.info("config successfully parsed and logger configured")

    # read profiles
    with open(cfg.profiles.path) as file:
        profiles = json.load(file)
    logger.info("profiles successfully read")

    # connect to database and choose table for saving profiles
    db = Database(cfg.db.url, cfg.db.table)
    logger.info("successfully connected to database")

    # init ssh client
    ssh = SSHClient()

    for profile in profiles:
        logger.info(f"starting to process profile {profile}")

        # parse host profile or skip if failure
        try:
            host = Host.model_validate(profile)
            logger.info("host profile successfully parsed")
        except ValidationError as err:
            logger.error(err)
            logger.warning("skipped, go to next")
            continue

        # collect all required host params or skip if failure
        try:
            ssh.exec_commands(host, cfg.ssh.commands)
            logger.info("successfully got host params")
        except TimeoutError as err:
            logger.error("connection time expired")
            logger.warning("skipped, go to next")
            continue
        except RuntimeError:
            logger.error("can not get all required params for host")
            logger.warning("skipped, go to next")
            continue
        except Exception as err:
            logger.error(err)
            logger.warning("skipped, go to next")
            continue

        # save host profiles to database or abort if failure
        try:
            db.save_profile(host, cfg.db.columns)
            logger.info("host profile successfully saved to database")
        except Exception as err:
            logger.error(err)
            exit(1)
