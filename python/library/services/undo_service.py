from src.exceptions.undo_exceptions import NoMoreUndosException, NoMoreRedosException

class FunctionCall:
    def __init__(self, function_name: callable, *function_params: any) -> None:
        self.__function_name = function_name
        self.__function_params = function_params

    def call(self) -> None:
        self.__function_name(*self.__function_params)

    def __call__(self, *args: any, **kwargs: any) -> None:
        self.call()

class Operation:
    def __init__(self, undo_function: FunctionCall, redo_function: FunctionCall) -> None:
        self.__undo_function = undo_function
        self.__redo_function = redo_function

    def undo(self) -> None:
        self.__undo_function()

    def redo(self) -> None:
        self.__redo_function()

class CascadedOperation:
    def __init__(self) -> None:
        self.__undo_function = []
        self.__redo_function = []

    def add_undo_function(self, undo_function: FunctionCall) -> None:
        self.__undo_function.append(undo_function)

    def add_redo_function(self, redo_function: FunctionCall) -> None:
        self.__redo_function.append(redo_function)

    def undo(self) -> None:
        for func in self.__undo_function:
            func()

    def redo(self) -> None:
        for func in self.__redo_function:
            func()

class UndoService:
    def __init__(self) -> None:
        self.__undo_stack = []
        self.__redo_stack = []

    def record_operation(self, operation: Operation) -> None:
        """Records a new operation and clears the redo stack."""
        self.__redo_stack.clear()
        self.__undo_stack.append(operation)

    def undo(self) -> None:
        """Undoes the last operation."""
        if not self.__undo_stack:
            raise NoMoreUndosException("No more undos available!")
        current_operation = self.__undo_stack.pop()
        current_operation.undo()
        self.__redo_stack.append(current_operation)

    def redo(self) -> None:
        """Redoes the last undone operation."""
        if not self.__redo_stack:
            raise NoMoreRedosException("No more redos available!")
        current_operation = self.__redo_stack.pop()
        current_operation.redo()
        self.__undo_stack.append(current_operation)
