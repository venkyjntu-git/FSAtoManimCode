from manim import *
class FSA:
    def __init__(self, st, inpu, tr, ins, f):
        self.states = st
        self.sigma = inpu
        self.delta = tr
        self.initialstate = ins
        self.finalstates = f
    def accepted_or_not(self, x):
        cs = self.initialstate
        for i in x:
            if (cs, i) in self.delta:
                cs = self.delta[(cs, i)]
            else:
                cs = 'rejected'
                break
        if cs in self.finalstates:
            return True
        else:
            return False
    def print_to_manim(self):
        out = open('manim.py', 'w')
        print(f'from manim import *', file=out)
        print('\n', file=out)
        print('class DrawFSA(Scene):', file=out)
        print('\tdef construct(self):', file=out)
        circle_positions = {
            1: [(0, 0)],
            2: [(2.5, 0), (-2.5, 0)],
            3: [(2.5, 1.5), (-2.5, 1.5), (0, -3)],
            4: [(2.5, -1.5), (-2.5, -1.5), (2.5, 1.5), (-2.5, 1.5)],
            5: [(0, 3), (-2, 1), (2, 1), (-2, -2), (2, -2)]
        }

        # if len(self.states) in circle_positions:
        #     positions = circle_positions[len(self.states)]
        #     for i in range(len(self.states)):
        #         x, y = positions[i]
        #         print(f'\t\tc{self.states[i]} = Circle(radius=0.7).shift({x}*RIGHT).shift({y}*UP)', file=out)
        #     print(f'\t\tself.play(', end='', file=out)
        #     for state in self.states:
        #         print(f'Create(c{state}), ', end='', file=out)
        #     print(')', file=out)
        # else:
        #     print('Number of states not supported.', file=out)

        text_positions = {
            1: [(0, 0)],
            2: [(2.5, 0), (-2.5, 0)],
            3: [(2.5, 1.5), (-2.5, 1.5), (0, -3)],
            4: [(2.5, -1.5), (-2.5, -1.5), (2.5, 1.5), (-2.5, 1.5)],
            5: [(0, 3), (-2, 1), (2, 1), (-2, -2), (2, -2)]
        }

        # if len(self.states) in text_positions:
        #     positions = text_positions[len(self.states)]
        #     for i in range(len(self.states)):
        #         x, y = positions[i]
        #         print(f'\t\tst_name_{self.states[i]} = Text("{self.states[i]}",font_size=24).shift({x}*RIGHT).shift({y}*UP)', file=out)
        #     print(f'\t\tself.play(', end='', file=out)
        #     for state in self.states:
        #         print(f'Write(st_name_{state}), ', end='', file=out)
        #     print(')', file=out)
        #  # Create arrows between states
        #     for start_state, end_state in self.delta.items():
        #         start_circle = circles[start_state]
        #         end_circle = circles[end_state]
        #         arrow = Arrow(start=start_circle, end=end_circle)
        #         self.play(GrowArrow(arrow))

        # if len(self.states) == 1:
        #     print(f'\t\tc{self.states[0]} = Circle(radius=0.7)',file=out)
        #     print(f'\t\tself.play(Create(c{self.states[0]}))', file=out)
        # elif len(self.states) == 2:
        #     print(f'\t\tc{self.states[0]} = Circle(radius=0.7).shift(2.5*LEFT)', file=out)
        #     print(f'\t\tc{self.states[1]} = Circle(radius=0.7).shift(2.5*RIGHT)',file=out)
        #     print(f'\t\tself.play(Create(c{self.states[0]}), Create(c{self.states[1]}))', file=out)
        # elif len(self.states) == 3:
        #     print(f'\t\tc{self.states[0]} = Circle(radius=0.7).shift(2.5*LEFT).shift(DOWN*1.5)', file=out)
        #     print(f'\t\tc{self.states[1]} = Circle(radius=0.7).shift(2.5*RIGHT).shift(DOWN*1.5)',file=out)
        #     print(f'\t\tc{self.states[2]} = Circle(radius=0.7).shift(2*UP)', file=out)
        #     print(f'\t\tself.play(Create(c{self.states[0]}), Create(c{self.states[1]}), Create(c{self.states[2]}))', file=out)
        # elif len(self.states) == 4:
        #     print(f'\t\tc{self.states[0]} = Circle(radius=0.7).shift(2.5*LEFT).shift(UP*1.5)', file=out)
        #     print(f'\t\tc{self.states[1]} = Circle(radius=0.7).shift(2.5*RIGHT).shift(UP*1.5)', file=out)
        #     print(f'\t\tc{self.states[2]} = Circle(radius=0.7).shift(2.5*LEFT).shift(DOWN*1.5)',file=out)
        #     print(f'\t\tc{self.states[3]} = Circle(radius=0.7).shift(2.5*RIGHT).shift(DOWN*1.5)',file=out)
        #     print(f'\t\tself.play(Create(c{self.states[0]}), Create(c{self.states[1]}), Create(c{self.states[2]}),Create(c{self.states[3]}))', file=out)
        # elif len(self.states) == 5:
        #     print(f'\t\tc{self.states[0]} = Circle(radius=0.6).shift(UP*3)', file=out)
        #     print(f'\t\tc{self.states[1]} = Circle(radius=0.6).shift(2*LEFT).shift(UP*1)', file=out)
        #     print(f'\t\tc{self.states[2]} = Circle(radius=0.6).shift(2*RIGHT).shift(UP*1)',file=out)
        #     print(f'\t\tc{self.states[3]} = Circle(radius=0.6).shift(2*LEFT).shift(DOWN*2)',file=out)
        #     print(f'\t\tc{self.states[4]} = Circle(radius=0.6).shift(2*RIGHT).shift(DOWN*2)',file=out)
        #     print(f'\t\tself.play(Create(c{self.states[0]}), Create(c{self.states[1]}), Create(c{self.states[2]}),Create(c{self.states[3]}),Create(c{self.states[4]}))', file=out)



        if len(self.states) in circle_positions:
            positions = circle_positions[len(self.states)]
            for i in range(len(self.states)):
                state = self.states[i]
                x, y = positions[i]
                print(f'\t\tc{state} = Circle(radius=0.7).shift({x}*RIGHT + {y}*UP)', file=out)
                if state in self.finalstates:
                    print(f'\t\tc{state}_inner = Circle(radius=0.5).shift({x}*RIGHT + {y}*UP)', file=out)
            print(f'\t\tself.play(', end='', file=out)
            for state in self.states:
                print(f'Create(c{state}), ', end='', file=out)
                if state in self.finalstates:
                    print(f'Create(c{state}_inner),', end='', file=out)
            print(')', file=out)
        else:
            print('Number of states not supported.', file=out)


        if len(self.states) in text_positions:
            positions = text_positions[len(self.states)]
            for i in range(len(self.states)):
                state = self.states[i]
                x, y = positions[i]
                print(f'\t\tst_name_{state} = Text("{state}", font_size=24).shift({x}*RIGHT + {y}*UP)', file=out)
            print(f'\t\tself.play(', end='', file=out)
            for state in self.states:
                print(f'Write(st_name_{state}), ', end='', file=out)
            print(')', file=out)

        for (start_state, input_symbol), end_state in self.delta.items():
            start_x, start_y = circle_positions[len(self.states)][self.states.index(start_state)]
            end_x, end_y = circle_positions[len(self.states)][self.states.index(end_state)]
            print(f'\t\tarrow_{start_state}_{end_state} = Arrow(start=c{start_state}.get_center(), end=c{end_state}.get_center(), buff=0.1)', file=out)
            print(f'\t\tarrow_{start_state}_{end_state}_label = Text("{input_symbol}", font_size=18).next_to(arrow_{start_state}_{end_state}, UP, buff=0.1)', file=out)
            print(f'\t\tself.play(GrowArrow(arrow_{start_state}_{end_state}), Write(arrow_{start_state}_{end_state}_label))', file=out)


        initial_x, initial_y = circle_positions[len(self.states)][self.states.index(self.initialstate)]
        print(f'\t\tinitial_arrow = Arrow(LEFT*3, c{self.initialstate}.get_center(), buff=0.1)', file=out)
        print(f'\t\tself.play(GrowArrow(initial_arrow))', file=out)
        out.close()
# Example usage
s1 = ['q0','q1']
i1 = ['0']
d1 = {('q0', '0'): 'q1', ('q1', '0'): 'q0'}
st1 = 'q0'
f1 = ['q1']
M1 = FSA(s1, i1, d1, st1, f1)
M1.print_to_manim()

# s1 = ['q0','q1','q2']
# i1 = ['0','1']
# d1 = {('q0','0'):'q1',('q0','1'):'q1',
#       ('q1','0'):'q2',('q1','1'):'q2',
#       ('q2','0'):'q0',('q2','1'):'q0'
# }
# st1 = 'q0'
# f1  = ['q0']
# M1 = FSA(s1,i1,d1,st1,f1)


# s1 = ['q0','q1','q2','q3']
# i1 = ['0','1']
# d1 = {('q0','0'):'q1',('q0','1'):'q1',
#       ('q1','0'):'q2',('q1','1'):'q2',
#       ('q2','0'):'q3',('q2','1'):'q3',
#       ('q3','0'):'q0',('q3','1'):'q0'
# }
# st1 = 'q0'
# f1  = ['q0']
# M2 = FSA(s1,i1,d1,st1,f1)
# M = M1.fsa_union(M2)
# x = input('enter string')
# print(M.accepted_or_not(x))
