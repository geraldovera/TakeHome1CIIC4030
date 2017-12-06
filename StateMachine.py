
# Class for handling the state machine.
class StateMachine():

    def __init__(self, states, initialState, transitions):
        self.states = states
        self.currState = initialState
        self.transitions = transitions
        self.accepted = False

    # Transitions from source state to target with trigger. Returns true if accepted, false otherwise.
    def transition(self, trigg):
        if not (trigg == 'a' or trigg == 'b'):
            return False

        else:
            for transition in self.transitions:
                if transition['src'] == self.currState and trigg == transition['trigger']:
                    self.prevState = self.currState
                    self.currState = transition['target']
                    self.currTrigg = trigg

                    if self.currState == 'D':
                        self.accepted = True

                    return True

            return False

    # Transitions through a regular expression. Returns true if accepted, false otherwise.
    def transitionRE(self, regExp):
        for letter in regExp:
            if not self.transition(letter):
                return False

        return True

    def getstate(self):
        return self.currState