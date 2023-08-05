from tantamount.astate import AState
from hippodamia_agent.states.event_ids import event_ids


class Onboarded(AState):
    sigint = None
    send_config = None
    deactivate_onboarding_response = None
    activate_last_will = None
    logger = None

    def __init__(self, logger, sigint):
        AState.__init__()
        self.sigint = sigint
        self.logger = logger
        self.logger.info("State 'Onboarded' created")

    def on_entry(self):
        self.logger.info("state on_entry: Onboarded")
        if self.sigint.is_set():
            return event_ids.sigint

        self.send_config()
        self.deactivate_onboarding_response()
        self.activate_last_will()

        return None

    def on_exit(self):
        self.logger.info("state on_exit: Onboarded")
        pass
