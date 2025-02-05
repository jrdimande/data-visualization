from plotly.graph_objs import Bar, Figure, Layout
from plotly import offline

class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.marks = [0, 0, 0, 0, 0, 0]
        self.colors = ['green'] * 6
        self.num_assess = 0



    # Function to add marks
    def add_mark(self, points):
        if self.num_assess <= 5:
            self.marks[self.num_assess] = points

            # Update the color based on the marks
            for i in range(2):
                if self.marks[i] < 25:
                    self.colors[i] = 'red'
                else:
                    self.colors[i] = 'green'

            if self.marks[2] < 50:
                self.colors[2] = 'red'
            else:
                self.colors[2] = 'green'

            if self.marks[3] < 25:
                self.colors[3] = 'red'
            else:
                self.colors[3] = 'green'

            if self.marks[4] < 50:
                self.colors[4] = 'red'
            else:
                self.colors[4] = 'green'

            if self.marks[5] < 300:
                self.colors[5] = 'red'
            else:
                self.colors[5] = 'green'






            self.num_assess += 1
            print("Mark added successfully")
        else:
            print("Exceeded the assessment limit")


    def  show_performance(self):
        assessments = ['Mini-teste1', 'Mini-teste2', 'Teste1', 'Mini-teste3', 'Teste2', 'Exam']
        data = [Bar(x=assessments, y=self.marks, marker_color=self.colors)]

        x_axis_config = {'title' : 'Assessments', 'dtick' : 1}
        y_axis_config = {'title' : 'Marks'}
        my_layout = Layout(title='Performance', xaxis=x_axis_config, yaxis=y_axis_config)
        offline.plot({'data' : data, 'layout' : my_layout}, filename='performance.html')









more = Subject("Math")
more.add_mark(50)
more.add_mark(25)
more.add_mark(100)
more.add_mark(23)
more.add_mark(40)
more.add_mark(360)
more.show_performance()










