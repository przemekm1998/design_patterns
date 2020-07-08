from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def _collect_source(self):
        pass

    @abstractmethod
    def _compile_to_object(self):
        pass

    @abstractmethod
    def _run(self):
        pass

    def compile_and_run(self):
        self._collect_source()
        self._compile_to_object()
        self._run()


class iOSCompiler(Compiler):
    def _collect_source(self):
        print("Collecting swift source code")

    def _compile_to_object(self):
        print("Compiling swift code to llvm bitcode")

    def _run(self):
        print("Program running on runtime env")


if __name__ == '__main__':
    ios = iOSCompiler()
    ios.compile_and_run()
