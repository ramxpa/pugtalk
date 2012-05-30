import collections
import webbrowser
from pygooglechart import PieChart3D

def draw_obama_chart():
    with open('obama.txt', 'r') as f:
        data_o = collections.Counter([line.split(',')[1].strip() for line in f.readlines()]).most_common()

    o_data = [app[1] for app in data_o][0:10]
    o_labels = [app[0] for app in data_o][0:10]
   
    obamaChart = PieChart3D(400, 100)
    obamaChart.add_data(o_data)
    obamaChart.set_pie_labels(o_labels)
    webbrowser.open_new_tab(obamaChart.get_url())    

def draw_romney_chart():
    with open('romney.txt', 'r') as f:
        data_r = collections.Counter([line.split(',')[1].strip() for line in f.readlines()]).most_common()

    r_data = [app[1] for app in data_r][0:10]
    r_labels = [app[0] for app in data_r][0:10]

    romneyChart = PieChart3D(500, 100)
    romneyChart.add_data(r_data)
    romneyChart.set_pie_labels(r_labels)
    webbrowser.open_new_tab(romneyChart.get_url())

def main():
    draw_obama_chart()
    draw_romney_chart()

if __name__ == '__main__':
    main()