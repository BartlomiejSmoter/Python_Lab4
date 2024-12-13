class State:
    def __init__(self, name, output=None):
        self.name = name
        self.output = output
        self.transitions = {}

    def add_transition(self, input_symbol, next_state, output=None):
        self.transitions[input_symbol] = (next_state, output)

    def get_next_state(self, input_symbol):
        return self.transitions.get(input_symbol, (None, None))


class MealyMachine:
    def __init__(self):
        self.states = {}
        self.initial_state = None

    def add_state(self, state):
        self.states[state.name] = state

    def set_initial_state(self, state_name):
        self.initial_state = self.states[state_name]

    def process_input(self, inputs):
        current_state = self.initial_state
        outputs = []

        for input_symbol in inputs:
            next_state, output = current_state.get_next_state(input_symbol)
            if next_state is None:
                raise ValueError(f"No transition defined for input '{input_symbol}' in state '{current_state.name}'.")

            outputs.append(output)
            current_state = self.states[next_state]

        return outputs


s0 = State("S0")
s1 = State("S1")

s0.add_transition("0", "S0", "0")
s0.add_transition("1", "S1", "1")
s1.add_transition("0", "S0", "1")
s1.add_transition("1", "S1", "0")

mealy_machine = MealyMachine()
mealy_machine.add_state(s0)
mealy_machine.add_state(s1)
mealy_machine.set_initial_state("S0")

inputs = "11001"
outputs = mealy_machine.process_input(inputs)

print(f"Input: {inputs}")
print(f"Output: {''.join(outputs)}")
