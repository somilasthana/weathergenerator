from refactor.contract.process import Process
from refactor.contract.report import SimulatorReporterInterface
from refactor.contract.simulator import SimulatorInterface
from refactor.simerror.contracterror import ContractException
from refactor.simerror.paramerror import InvalidParamException
from refactor.simerror.misc import EmptyTaskListException
from refactor.simerror.misc import TaskOutNoneException
from refactor.simlog.printlog import printlog


class BasicSimulator(SimulatorInterface):

    def __init__(self):
        """
        Initializes the Tasks List which will run
        """
        self.tasklet = [] # Should persistence be delegated
        self.num_iterations = 0
        self.max_task_capacity = 0
        self.simulator_reporter = None

    def initialize(self, num_iterations, max_task_capacity=1000):
        """
        Set the number of times Simulator runs and set number of task it can support.
        :param num_iterations: sets number of times each task's run will be involved
        :param max_task_capacity: maximum cap of task to avoid
        :return: None
        """

        self.num_iterations = num_iterations
        self.max_task_capacity = max_task_capacity
        printlog("BasicSimulator", "will be running with num_iterations = {0}, max_task_capacity = {1}".format(self.num_iterations,
                                                                                                               self.max_task_capacity))

        if self.num_iterations < 0:
            raise InvalidParamException("num_iterations should be greater than 0")
        if self.max_task_capacity < 0:
            raise InvalidParamException("max_task_capacity should be greater than 0")

    def activate(self, sim_task):
        """
        Attach a task to Simulator, the generic simulator does not care on what type of task it enforces each Task
        should implement "Process" abstract interfaces "run_method" and "get_status".

        Simulator has minimal resources so only max_task_capacity number of tasks are added to run.
        :param sim_task: Any concrete class that implements Process abstract class
        :return:
        """

        if sim_task is None:
            printlog("Simulation", "Simulator expects sim_task object found None instead ")
            ContractException("Simulator expects sim_task object found None instead")

        if len(self.tasklet) <= self.max_task_capacity:
            self.tasklet.append(sim_task)
        else:
            """
            This simulator simply ignores tasks once the max_task_capacity is reached but logs an error.
            """
            printlog("Simulator", "Cannot add tasks any more maximum capacity reached {}".format(self.max_task_capacity))

    def simulate(self, reporter):
        """
        Before beginning the simulation, the Simulator needs to know what to do with the output produced
        by each Task.
        Task Output Handler class is responsible to doing something with task state.
        This something can be
        1. Storing the state in a file
        2. Streaming the state on Rabbitmq or Apache Kafka

        In Weather simulation each task will provide weather properties.
        :param sim_handler:
        :return: None
        """

        if len(self.tasklet) == 0:
            printlog("Simulator", "Simulator does not has any tasks to run")
            raise EmptyTaskListException("Simulator does not has any tasks to run")

        self.simulator_reporter = reporter

        if self.simulator_reporter is None:
            printlog("Simulator", "Simulator does not understand what do with task's output")

        printlog("Simulator", "Simulator will run for {} ticks".format(self.num_iterations))
        run_iterations = self.num_iterations

        while run_iterations > 0:
            printlog("Simulator", "Running iteration no. {}".format(self.num_iterations - run_iterations))

            for task in self.tasklet:
                task.run_method()
                state = task.get_state()

                if state is None:
                    raise TaskOutNoneException("No output from Task" + str(task))

                if self.simulator_reporter is not None:
                    self.simulator_reporter.save_state(state)

            run_iterations -= 1

    def stop(self):
        """
        First we cleanup on each task any resource it may acquired.
        Finally we cleanup on task_output handler.
        :return:
        """
        for task in self.tasklet:
            task.cleanup()
        if self.simulator_reporter:
            self.simulator_reporter.cleanup()
