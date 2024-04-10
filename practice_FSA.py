from manim import *
class FSA:
    def __init__(self,states,input_symbols,transition_function,initial_state,final_states):
        self.states = states
        self.sigma = input_symbols
        self.delta = transition_function
        self.initialstate = initial_state
        self.finalstates = final_states
    def accepted_or_not(self, input_string):
        current_state = self.initialstate
        for symbol in input_string:
            if (current_state, symbol) in self.delta:
                current_state = self.delta[(current_state, symbol)]
            else:
                return False
        return current_state in self.finalstates
    def print_to_manim(self):
        out = open('manim1.py', 'w')
        print(f'from manim import *', file=out)
        print('\n', file=out)
        print('class DrawFSA(Scene):', file=out)
        print('\tdef construct(self):', file=out)

        print("\t\tstart_text = Text('Animation for FSA using Manim', font_size=45)",file=out)
        print("\t\tstart_text1= Text('The initial state is represented with YELLOW colour', font_size=38,font='Times New Roman').shift(DOWN*2)",file=out)
        print("\t\tself.play(Write(start_text),Write(start_text1))",file=out)
        print("\t\tself.play(FadeOut(start_text),FadeOut(start_text1))",file=out)
        print("\t\tself.wait(1) ",file=out)

        circle_positions = {
            1: [(0, 0)],
            2: [(2.5, 0), (-2.5, 0)],
            3: [(2.5, 1.5), (-2.5, 1.5), (2.5, -1.5)],
            4: [(-2, 1.5),(2, 1.5),(2.5, -1.5), (-2.5, -1.5)],
            5: [(0, 3), (-2, 1), (2, 1), (-2, -2), (2, -2)]
        }

        if len(self.states) in circle_positions:
            positions = circle_positions[len(self.states)]
            for i in range(len(self.states)):
                state = self.states[i]
                x, y = positions[i]
                if state == self.initialstate:
                    print(f'\t\tc{state} = Circle(radius=0.7, color=YELLOW).shift({x}*RIGHT + {y}*UP)', file=out)
                else:
                    print(f'\t\tc{state} = Circle(radius=0.7, color=WHITE).shift({x}*RIGHT + {y}*UP)', file=out)
                if state in self.finalstates:
                    print(f'\t\tc{state}_inner = Circle(radius=0.5,color=BLUE_C).shift({x}*RIGHT + {y}*UP)', file=out)
            print(f'\t\tself.add(', end='', file=out)
            for state in self.states:
                print(f'c{state}, ', end='', file=out)
                if state in self.finalstates:
                    print(f'c{state}_inner,', end='', file=out)
            print(')', file=out)
        else:
            print('Number of states not supported.', file=out)

        text_positions = {
            1: [(0, 0)],
            2: [(2.5, 0), (-2.5, 0)],
            3: [(2.5, 1.5), (-2.5, 1.5), (2.5, -1.5)],
            4: [(-2, 1.5),(2, 1.5),(2.5, -1.5), (-2.5, -1.5)],
            5: [(0, 3), (-2, 1), (2, 1), (-2, -2), (2, -2)]
        }

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
        
        # print(f"\t\tinitial_state_text= Text('Initial state',color=YELLOW_B,font_size=28)",file=out)
        # print(f"\t\tinitial_state_text.next_to(c{self.initialstate}, DOWN)",file=out)
        # print("\t\tself.play(Write(initial_state_text),run_time=0.6)",file=out)

        for (start_state, input_symbol), end_state in self.delta.items():
            start_idx = self.states.index(start_state)
            end_idx = self.states.index(end_state)

            if len(self.states) == 1:
                if start_state == self.states[0]:
                    print(f"\t\tself_arrow = CurvedArrow(start_point=RIGHT, end_point=LEFT, angle=PI).shift(c{start_state}.get_top())", file=out)
                    print(f"\t\tself_arrow_label = Text('{input_symbol}', font_size=22).next_to(self_arrow, UP)", file=out)
                    print(f"\t\tself.add(self_arrow, self_arrow_label)", file=out)
                    print(f"initial_arrow = Arrow(LEFT*3, c{start_state}.get_left(), color=YELLOW)",file=out)
                    print(f"self.add(initial_arrow)",file=out)

            elif len(self.states) == 2:
                if start_state==end_state:
                    print(f"\t\tself_arrow = CurvedArrow(start_point=RIGHT, end_point=LEFT, angle=PI).shift(c{start_state}.get_top())", file=out)
                    print(f"\t\tself_arrow_label = Text('{input_symbol}', font_size=22).next_to(self_arrow,UP)", file=out)
                    print(f"\t\tself.add(self_arrow, self_arrow_label)", file=out)
                # if start_state == end_state:
                #     if start_state == self.states[0]:
                #         print(f"\t\tself_arrow = CurvedArrow(start_point=RIGHT, end_point=LEFT, angle=PI).shift(c{start_state}.get_top())", file=out)
                #         print(f"\t\tself_arrow_label = Text('{input_symbol}', font_size=24).next_to(self_arrow, RIGHT, buff=0.1)", file=out)
                #         print(f"\t\tself.add(self_arrow, self_arrow_label)", file=out)
                #     elif start_state == self.states[1]:
                #         print(f"\t\tself_arrow = CurvedArrow(start_point=RIGHT, end_point=LEFT, angle=PI).shift(c{start_state}.get_top())", file=out)
                #         print(f"\t\tself_arrow_label = Text('{input_symbol}', font_size=24).next_to(self_arrow, RIGHT, buff=0.1)", file=out)
                #         print(f"\t\tself.add(self_arrow, self_arrow_label)", file=out)
                elif start_state!=end_state:
                    # if start_state == self.states[0] and end_state == self.states[1]:
                    #     print(f"\t\tarrow = Arrow(c{start_state}.get_center(), c{end_state}.get_center(), buff=0.7).shift(0.3*UP)", file=out)
                    #     print(f"\t\tarrow_label = Text('{input_symbol}', font_size=18).next_to(arrow, UP)", file=out)
                    #     print(f"\t\tself.add(arrow, arrow_label)", file=out)
                    # elif start_state == self.states[1] and end_state == self.states[0]:
                    #     print(f"\t\tarrow = Arrow(c{start_state}.get_center(), c{end_state}.get_center(), buff=0.7).shift(0.3*DOWN)", file=out)
                    #     print(f"\t\tarrow_label = Text('{input_symbol}', font_size=18).next_to(arrow, DOWN)", file=out)
                    #     print(f"\t\tself.add(arrow, arrow_label)", file=out)
                    print(f"\t\tarrow = Arrow(c{start_state}.get_center(), c{end_state}.get_center(), buff=0.7)",file=out)
                    print(f"\t\tarrow_label = Text('{input_symbol}', font_size=18)",file=out)
                    if start_idx < end_idx:
                        print("\t\tarrow.shift(UP*0.4)",file=out)
                        print("\t\tarrow_label.next_to(arrow, UP)",file=out)
                    elif start_idx > end_idx:
                        print("\t\tarrow.shift(DOWN*0.4)",file=out)
                        print("\t\tarrow_label.next_to(arrow, DOWN)",file=out)
                    print("\t\tself.add(arrow, arrow_label)",file=out)
                
            elif len(self.states) == 3:
                if start_state == end_state:
                    if start_state=='q1' or start_state=='q0':
                        print(f"\t\tself_arrow = CurvedArrow(start_point=RIGHT, end_point=LEFT, angle=PI).shift(c{start_state}.get_top())", file=out)
                        print(f"\t\tself_arrow_label = Text('{input_symbol}', font_size=22).next_to(self_arrow,UP)", file=out)
                        print(f"\t\tself.add(self_arrow, self_arrow_label)", file=out)
                        print("\n",file=out)
                    elif start_state == 'q2':
                        print(f"\t\tself_arrow = CurvedArrow(start_point=RIGHT, end_point=LEFT, angle=-PI).shift(c{start_state}.get_bottom())", file=out)
                        print(f"\t\tself_arrow_label = Text('{input_symbol}', font_size=22).next_to(self_arrow,DOWN)", file=out)
                        print(f"\t\tself.add(self_arrow, self_arrow_label)", file=out)
                        print("\n\n",file=out)
                elif start_state in ['q0','q2'] and end_state in ['q0','q2']:
                    print(f"\t\tarrow = Arrow(c{start_state}.get_center(), c{end_state}.get_center(), buff=0.8)",file=out)
                    print(f"\t\tarrow_label = Text('{input_symbol}', font_size=20)",file=out)
                    if start_idx < end_idx:
                        print("\t\tarrow.shift(LEFT*0.4)",file=out)
                        print("\t\tarrow_label.shift(arrow.get_center()+RIGHT*0.3)",file=out)
                    elif start_idx > end_idx:
                        print("\t\tarrow.shift(RIGHT*0.4)",file=out)
                        print("\t\tarrow_label.shift(arrow.get_center()+RIGHT*0.3)",file=out)
                    print("\t\tself.add(arrow, arrow_label)",file=out)
                    print("\n",file=out)
                else:
                    print(f"\t\tarrow = Arrow(c{start_state}.get_center(), c{end_state}.get_center(), buff=0.8)",file=out)
                    print(f"\t\tarrow_label = Text('{input_symbol}', font_size=20)",file=out)
                    if start_idx < end_idx:
                        print("\t\tarrow.shift(UP*0.5)",file=out)
                        print("\t\tarrow_label.shift(arrow.get_center()+UP*0.3+LEFT*0.3)",file=out)
                    elif start_idx > end_idx:
                        print("\t\tarrow.shift(DOWN*0.5)",file=out)
                        print("\t\tarrow_label.shift(arrow.get_center()+UP*0.3)",file=out)
                    print("\t\tself.add(arrow, arrow_label)",file=out)
                    print("\n",file=out)
                
            elif len(self.states) == 4:
                if start_state == end_state:
                    if start_state=='q1' or start_state=='q0':
                        print(f"\t\tself_arrow = CurvedArrow(start_point=RIGHT, end_point=LEFT, angle=PI).shift(c{start_state}.get_top())", file=out)
                        print(f"\t\tself_arrow_label = Text('{input_symbol}', font_size=22).next_to(self_arrow,UP)", file=out)
                        print(f"\t\tself.add(self_arrow, self_arrow_label)", file=out)
                        print("\n\n",file=out)
                    elif start_state == 'q2' or start_state == 'q3':
                        print(f"\t\tself_arrow = CurvedArrow(start_point=RIGHT, end_point=LEFT, angle=-PI).shift(c{start_state}.get_bottom())", file=out)
                        print(f"\t\tself_arrow_label = Text('{input_symbol}', font_size=22).next_to(self_arrow,DOWN)", file=out)
                        print(f"\t\tself.add(self_arrow, self_arrow_label)", file=out)
                        print("\n\n",file=out)
                elif start_state != end_state:
                    print(f"\t\tarrow = Arrow(c{start_state}.get_center(), c{end_state}.get_center(), buff=0.9)",file=out)
                    print(f"\t\tarrow_label = Text('{input_symbol}', font_size=20)",file=out)
                    if start_idx < end_idx:
                        print("\t\tarrow.shift(UP*0.5)",file=out)
                        print("\t\tarrow_label.next_to(arrow,UP*1)",file=out)
                    elif start_idx > end_idx:
                        print("\t\tarrow.shift(DOWN*0.5)",file=out)
                        print("\t\tarrow_label.next_to(arrow, DOWN*1)",file=out)
                    print("\t\tself.add(arrow, arrow_label)",file=out)
                    print("\n\n\n",file=out)
        
        print( "\t\tself.wait(5)",file=out)
        out.close()


s1 = ['q0','q1','q2']
i1 = ['0', '1']
#3 states
d1 = {
    ('q0', '0'): 'q0', ('q1', '0'): 'q1', ('q2', '0'): 'q2',
    ('q0', '1'): 'q1', ('q1', '1'): 'q0',
    ('q0', '2'): 'q2', ('q2', '1'): 'q0',
    ('q1', '3'): 'q2', ('q2', '5'): 'q1',
}

#for 4 states
# d1 = {
#     ('q0', '0'): 'q0', ('q1', '0'): 'q1', ('q2', '0'): 'q2',('q3', '9'): 'q3',
#     ('q0', '1'): 'q1', ('q1', '1'): 'q0',
#     ('q0', '2'): 'q3', ('q3', '1'): 'q0',
#     ('q3', '3'): 'q2', ('q2', '4'): 'q3',
#     ('q1', '7'): 'q2', ('q2', '5'): 'q1',
# }

st1 = 'q0'
f1 = ['q1']
M1 = FSA(s1, i1, d1, st1, f1)
M1.print_to_manim()
