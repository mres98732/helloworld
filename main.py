"""Main module of mres98732/helloworld Kytos Network Application.

My first napp
"""

from kytos.core import KytosNApp, log

from napps.mres98732.helloworld import settings


class Main(KytosNApp):
    """Main class of mres98732/helloworld NApp.

    This class is the entry point for this NApp.
    """

    def setup(self):
        """Replace the '__init__' method for the KytosNApp subclass.

        The setup method is automatically called by the controller when your
        application is loaded.

        So, if you have any setup routine, insert it here.
        """
        log.info("Hello world! Now, I'm loaded!")

    def execute(self):
        """Run after the setup method execution.

        You can also use this method in loop mode if you add to the above setup
        method a line like the following example:

            self.execute_as_loop(30)  # 30-second interval.
        """
        log.info("Hello world! I'm being executed!")

    def shutdown(self):
        """Run when your NApp is unloaded.

        If you have some cleanup procedure, insert it here.
        """
        log.info("Bye world!")

