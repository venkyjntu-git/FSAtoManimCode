class FSA:
    def __init__(self,states,input_symbols,transition_function,initial_state,final_states):
        self.states = states
        self.sigma = input_symbols
        self.delta = transition_function
        self.initialstate = initial_state
        self.finalstates = final_states
        
    def print_to_manim(self):
        input_string= input("Enter the string for FSA : ")
        current_state = self.initialstate
        for symbol in input_string:
            if (current_state, symbol) in self.delta:
                current_state = self.delta[(current_state, symbol)]
            else:
                break
        if current_state in self.finalstates:
            print(f"{input_string} string is accepted. Run the manim_fsa.py file to see the animation\n\n\n")
        else:
            print(f"\n{input_string}String is not accepted.\nSee the manim animation for the given string\n\n\n")

        
        out = open('manim_fsa.py', 'w')
        print(f'from manim import *', file=out)
        print('\n\n', file=out)

        print('class DrawFSA(Scene):', file=out)
        print('\tdef construct(self):', file=out)
        print("\t\tstart_text = Text('Animation for FSA using Manim', font_size=45)",file=out)
        print("\t\tstart_text1= Text('The initial state is represented with YELLOW colour', font_size=38,font='Times New Roman',color=YELLOW).shift(DOWN*2)",file=out)
        print("\t\tself.play(Write(start_text),Write(start_text1))",file=out)
        print("\t\tself.play(FadeOut(start_text),FadeOut(start_text1))",file=out)
        print("\t\tself.wait(2) ",file=out)

        circle_positions = {
            1: [(0, 0)],
            2: [(-2.5, 0), (2.5, 0)],
            3: [(2.5, 1.5), (-2.5, 1.5), (2.5, -1.5)],
            4: [(-2, 1.5),(2, 1.5),(2, -1.5), (-2, -1.5)],
            5: [(0, 3), (-2, 1), (2, 1), (-2, -2), (2, -2)],
        }

        if len(self.states) in circle_positions:
            positions = circle_positions[len(self.states)]
            for i in range(len(self.states)):
                state = self.states[i]
                x, y = positions[i]
                if state == self.initialstate:
                    print(f'\t\tc{state} = Circle(radius=0.7, color=YELLOW).shift({x}*RIGHT + {y}*UP)', file=out)#inital state
                else:
                    print(f'\t\tc{state} = Circle(radius=0.7, color=WHITE).shift({x}*RIGHT + {y}*UP)', file=out)#circle states
                if state in self.finalstates:
                    print(f'\t\tc{state}_inner = Circle(radius=0.6,color=BLUE_C).shift({x}*RIGHT + {y}*UP)', file=out)#final states
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
            2: [(-2.5, 0), (2.5, 0)],
            3: [(2.5, 1.5), (-2.5, 1.5), (2.5, -1.5)],
            4: [(-2, 1.5),(2, 1.5),(2, -1.5), (-2, -1.5)]
        }
        if len(self.states) in text_positions:
            positions1 = text_positions[len(self.states)]
            for i in range(len(self.states)):
                state = self.states[i]
                x, y = positions1[i]
                print(f'\t\tst_name_{state} = Text("{state}", font_size=24).shift({x}*RIGHT + {y}*UP)', file=out)
            print(f'\t\tself.play(', end='', file=out)
            for state in self.states:
                print(f'Write(st_name_{state}), ', end='', file=out)
            print(')', file=out) 
        
        for (start_state, input_symbol), end_state in self.delta.items():
            if input_symbol in self.sigma:
                start_idx =self.states.index(start_state)
                end_idx = self.states.index(end_state)
                print(f"\t\tstart_idx = {self.states.index(start_state)}",file=out)
                print(f"\t\tend_idx = {self.states.index(end_state)}",file=out)
                if len(self.states) == 1:
                    if start_state == self.states[0]:
                        print(f"\t\tself_arrow = CurvedArrow(start_point=RIGHT, end_point=LEFT, angle=PI).shift(c{start_state}.get_top())", file=out)
                        print(f"\t\tself_arrow_label = Text('{input_symbol}', font_size=22).next_to(self_arrow, UP)", file=out)
                        print(f"\t\tself.add(self_arrow, self_arrow_label)", file=out)
                        print(f"\t\tinitial_arrow = Arrow(LEFT*3, c{start_state}.get_left(), color=YELLOW)",file=out)
                        print(f"\t\tself.add(initial_arrow)",file=out)
                
                elif len(self.states) == 2:
                    if start_state==end_state:
                        print(f"\t\tself_arrow_{start_state}{end_state} = CurvedArrow(start_point=RIGHT, end_point=LEFT, angle=PI).shift(c{start_state}.get_top())", file=out)
                        print(f"\t\tself_arrow_label_{start_state}{end_state} = Text('{input_symbol}', font_size=22).next_to(self_arrow_{start_state}{end_state},UP)", file=out)
                        print(f"\t\tself.add(self_arrow_{start_state}{end_state}, self_arrow_label_{start_state}{end_state})", file=out)
                        print("\n\n",file=out)
                    else:
                        print(f"\t\tarrow_{start_state}{end_state} = Arrow(c{start_state}.get_center(), c{end_state}.get_center(), buff=0.7)",file=out)
                        print(f"\t\tarrow_label_{start_state}{end_state} = Text('{input_symbol}', font_size=18)",file=out)
                        # if start_idx < end_idx:
                        #     print(f"\t\tarrow_{start_state}{end_state}.shift(UP*0.4)",file=out)
                        #     print(f"\t\tarrow_label_{start_state}{end_state}.next_to(arrow_{start_state}{end_state}, UP)",file=out)
                        # else:
                        #     print(f"\t\tarrow_{start_state}{end_state}.shift(DOWN*0.4)",file=out)
                        #     print(f"\t\tarrow_label_{start_state}{end_state}.next_to(arrow_{start_state}{end_state}, DOWN)",file=out)
                        # print(f"\t\tself.add(arrow_{start_state}{end_state}, arrow_label_{start_state}{end_state})",file=out)
                        shift_direction = "UP" if start_idx < end_idx else "DOWN"
                        print(f"\t\tarrow_{start_state}{end_state}.shift({shift_direction}*0.4)", file=out)
                        print(f"\t\tarrow_label_{start_state}{end_state}.next_to(arrow_{start_state}{end_state}, {shift_direction})", file=out)
                        print(f"\t\tself.add(arrow_{start_state}{end_state}, arrow_label_{start_state}{end_state})\n\n", file=out)

                        print("\n\n",file=out)


                elif len(self.states) == 3:
                    if start_state == end_state:
                        if start_state==self.states[1] or start_state==self.states[0]:
                            print(f"\t\tself_arrow_{start_state}{end_state} = CurvedArrow(start_point=RIGHT, end_point=LEFT, angle=PI).shift(c{start_state}.get_top())", file=out)
                            print(f"\t\tself_arrow_label_{start_state}{end_state} = Text('{input_symbol}', font_size=22).next_to(self_arrow_{start_state}{end_state},UP)", file=out)
                            print(f"\t\tself.add(self_arrow_{start_state}{end_state}, self_arrow_label_{start_state}{end_state})", file=out)
                            print("\n",file=out)
                        elif start_state == self.states[2]:
                            print(f"\t\tself_arrow_{start_state}{end_state} = CurvedArrow(start_point=RIGHT, end_point=LEFT, angle=-PI).shift(c{start_state}.get_bottom())", file=out)
                            print(f"\t\tself_arrow_label_{start_state}{end_state} = Text('{input_symbol}', font_size=22).next_to(self_arrow_{start_state}{end_state},DOWN)", file=out)
                            print(f"\t\tself.add(self_arrow_{start_state}{end_state}, self_arrow_label_{start_state}{end_state})", file=out)
                            print("\n\n",file=out)
                    elif start_state in [self.states[0],self.states[2]] and end_state in [self.states[0],self.states[2]]:
                        print(f"\t\tarrow_{start_state}{end_state} = Arrow(c{start_state}.get_center(), c{end_state}.get_center(), buff=0.8)",file=out)
                        print(f"\t\tarrow_label_{start_state}{end_state} = Text('{input_symbol}', font_size=20)",file=out)
                        if start_idx < end_idx:
                            print(f"\t\tarrow_{start_state}{end_state}.shift(LEFT*0.4)",file=out)
                            print(f"\t\tarrow_label_{start_state}{end_state}.shift(arrow_{start_state}{end_state}.get_center()+RIGHT*0.3)",file=out)
                        elif start_idx > end_idx:
                            print(f"\t\tarrow_{start_state}{end_state}.shift(RIGHT*0.4)",file=out)
                            print(f"\t\tarrow_label_{start_state}{end_state}.shift(arrow_{start_state}{end_state}.get_center()+RIGHT*0.3)",file=out)
                        print(f"\t\tself.add(arrow_{start_state}{end_state}, arrow_label_{start_state}{end_state})",file=out)
                        print("\n",file=out)
                    else:
                        print(f"\t\tarrow_{start_state}{end_state} = Arrow(c{start_state}.get_center(), c{end_state}.get_center(), buff=0.8)",file=out)
                        print(f"\t\tarrow_label_{start_state}{end_state} = Text('{input_symbol}', font_size=20)",file=out)
                        if start_idx < end_idx:
                            print(f"\t\tarrow_{start_state}{end_state}.shift(UP*0.5)",file=out)
                            print(f"\t\tarrow_label_{start_state}{end_state}.shift(arrow_{start_state}{end_state}.get_center()+UP*0.3+RIGHT*0.3)",file=out)
                        elif start_idx > end_idx:
                            print(f"\t\tarrow_{start_state}{end_state}.shift(DOWN*0.5)",file=out)
                            print(f"\t\tarrow_label_{start_state}{end_state}.shift(arrow_{start_state}{end_state}.get_center()+UP*0.3)",file=out)
                        print(f"\t\tself.add(arrow_{start_state}{end_state}, arrow_label_{start_state}{end_state})",file=out)
                        print("\n",file=out)


                elif len(self.states) == 4:
                    if start_state == end_state:
                        if start_state==self.states[1] or start_state==self.states[0]:
                            print(f"\t\tself_arrow_{start_state}{end_state} = CurvedArrow(start_point=RIGHT, end_point=LEFT, angle=PI).shift(c{start_state}.get_top())", file=out)
                            print(f"\t\tself_arrow_label_{start_state}{end_state} = Text('{input_symbol}', font_size=22).next_to(self_arrow_{start_state}{end_state},UP)", file=out)
                            print(f"\t\tself.add(self_arrow_{start_state}{end_state}, self_arrow_label_{start_state}{end_state})", file=out)
                            print("\n",file=out)
                        elif start_state == self.states[2] or start_state==self.states[3]:
                            print(f"\t\tself_arrow_{start_state}{end_state} = CurvedArrow(start_point=RIGHT, end_point=LEFT, angle=-PI).shift(c{start_state}.get_bottom())", file=out)
                            print(f"\t\tself_arrow_label_{start_state}{end_state} = Text('{input_symbol}', font_size=22).next_to(self_arrow_{start_state}{end_state},DOWN)", file=out)
                            print(f"\t\tself.add(self_arrow_{start_state}{end_state}, self_arrow_label_{start_state}{end_state})", file=out)
                            print("\n\n",file=out)
                    elif (start_state, end_state) in [(self.states[0], self.states[3]), (self.states[3], self.states[0]), (self.states[1], self.states[2]), (self.states[2], self.states[1])]:
                        print(f"\t\tarrow_{start_state}{end_state} = Arrow(c{start_state}.get_center(), c{end_state}.get_center(), buff=0.9)",file=out)
                        print(f"\t\tarrow_label_{start_state}{end_state} = Text('{input_symbol}', font_size=21)",file=out)
                        if start_idx < end_idx:
                            print(f"\t\tarrow_{start_state}{end_state}.shift(LEFT*0.3)",file=out)
                            print(f"\t\tarrow_label_{start_state}{end_state}.shift(arrow_{start_state}{end_state}.get_center()+LEFT*0.3)",file=out)
                        elif start_idx > end_idx:
                            print(f"\t\tarrow_{start_state}{end_state}.shift(RIGHT*0.3)",file=out)
                            print(f"\t\tarrow_label_{start_state}{end_state}.shift(arrow_{start_state}{end_state}.get_center()+RIGHT*0.4)",file=out)
                        print(f"\t\tself.add(arrow_{start_state}{end_state}, arrow_label_{start_state}{end_state})",file=out)
                        print("\n",file=out)
                    elif (start_state, end_state) in [(self.states[0], self.states[2]), (self.states[2], self.states[0])]:
                        print(f"\t\tarrow_{start_state}{end_state} = Arrow(c{start_state}.get_center(), c{end_state}.get_center(), buff=0.9)",file=out)
                        print(f"\t\tarrow_label_{start_state}{end_state} = Text('{input_symbol}', font_size=20)",file=out)
                        if start_idx < end_idx:
                            print(f"\t\tarrow_{start_state}{end_state}.shift(UP*0.4)",file=out)
                            print(f"\t\tarrow_label_{start_state}{end_state}.shift(arrow_{start_state}{end_state}.get_center()+DOWN*0.3)",file=out)
                        elif start_idx > end_idx:
                            print(f"\t\tarrow_{start_state}{end_state}.shift(DOWN*0.4)",file=out)
                            print(f"\t\tarrow_label_{start_state}{end_state}.shift(arrow_{start_state}{end_state}.get_center()+UP*0.5+LEFT*0.4)",file=out)
                        print(f"\t\tself.add(arrow_{start_state}{end_state}, arrow_label_{start_state}{end_state})",file=out)
                        print("\n",file=out)
                    elif (start_state, end_state) in [(self.states[2], self.states[3]), (self.states[3], self.states[2])]:
                        print(f"\t\tarrow_{start_state}{end_state} = Arrow(c{start_state}.get_center(), c{end_state}.get_center(), buff=0.9)",file=out)
                        print(f"\t\tarrow_label_{start_state}{end_state} = Text('{input_symbol}', font_size=21)",file=out)
                        if start_idx > end_idx:
                            print(f"\t\tarrow_{start_state}{end_state}.shift(UP*0.35)",file=out)
                            print(f"\t\tarrow_label_{start_state}{end_state}.shift(arrow_{start_state}{end_state}.get_center()+DOWN*0.3)",file=out)
                        elif start_idx < end_idx:
                            print(f"\t\tarrow_{start_state}{end_state}.shift(DOWN*0.4)",file=out)
                            print(f"\t\tarrow_label_{start_state}{end_state}.shift(arrow_{start_state}{end_state}.get_center()+DOWN*0.3+RIGHT*0.5)",file=out)
                        print(f"\t\tself.add(arrow_{start_state}{end_state}, arrow_label_{start_state}{end_state})",file=out)
                        print("\n",file=out)
                    else:
                        print(f"\t\tarrow_{start_state}{end_state} = Arrow(c{start_state}.get_center(), c{end_state}.get_center(), buff=0.9)",file=out)
                        print(f"\t\tarrow_label_{start_state}{end_state} = Text('{input_symbol}', font_size=21)",file=out)
                        if start_idx < end_idx:
                            print(f"\t\tarrow_{start_state}{end_state}.shift(UP*0.3)",file=out)
                            print(f"\t\tarrow_label_{start_state}{end_state}.shift(arrow_{start_state}{end_state}.get_center()+UP*0.3)",file=out)
                        elif start_idx > end_idx:
                            print(f"\t\tarrow_{start_state}{end_state}.shift(DOWN*0.3)",file=out)
                            print(f"\t\tarrow_label_{start_state}{end_state}.shift(arrow_{start_state}{end_state}.get_left()+DOWN*0.6+RIGHT*0.2)",file=out)
                        print(f"\t\tself.add(arrow_{start_state}{end_state}, arrow_label_{start_state}{end_state})",file=out)
                        print("\n",file=out)
                
        current_state = self.initialstate
        for symbol in input_string:
            if (current_state, symbol) in self.delta:
                end_state = self.delta[(current_state, symbol)]
                if current_state==end_state:
                    print(f"\t\tself.play(Create(self_arrow_{current_state}{end_state}), Write(self_arrow_label_{current_state}{end_state}))", file=out)
                else:
                    print(f"\t\tself.play(Create(arrow_{current_state}{end_state}), Write(arrow_label_{current_state}{end_state}))", file=out)
                current_state = end_state
                print(f"\t\tself.wait(0.5)", file=out)
            else:
                print("\t\t#Transition not defined for current state and symbol",file=out)
                break

        if current_state in self.finalstates:
            for state in self.finalstates:
                print(f"\t\tc{state}_inner.set_fill(GREEN, opacity=0.5)", file=out)
            print(f"\t\ta = Text(f'{input_string} is accepted', font_size=24).shift(DOWN*3+LEFT*1)",file=out)
            print(f"\t\tself.play(Write(a))", file=out)
        else:
            print(f"\t\tc{self.initialstate}.set_fill(RED, opacity=0.5)", file=out)
            print(f"\t\tb = Text(f'{input_string} is not accepted', font_size=24).shift(DOWN*3+LEFT*1)",file=out)
            print(f"\t\tself.play(Write(b))", file=out)
        print("\t\tself.wait(1)", file=out)
        print( "\t\tself.wait(5)",file=out)
        out.close()

#->No:of states=3
#Machine Aim: Strings which are ends with ab
s=['q0','q1','q2']
i=['a','b']
#Transitions:
d={('q0','a'):'q1',('q0','b'):'q0',('q1','a'):'q1',('q1','b'):'q2',('q2','a'):'q1',('q2','b'):'q0'}
st='q0'
f=['q2']
M1 = FSA(s, i, d, st, f)
M1.print_to_manim()
