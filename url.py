import PySimpleGUI as sg
from web import get_html_content,parse_html_using_tag
from webs import get_statistics

layout=[
    [sg.Text("Web page analyzer", font=("Arial", 14))],
    [sg.Text("Enter URL",font=("Arial",14)),sg.InputText("",font=("Arial",14),key='url'),
     sg.Button("Get Data",font=("Arial",14),key='get')],
    [sg.Multiline("",font=("Arial",14),size=(60,15),key='output')]

]

def get_details(url):
    """ Contain from webpage by url and to find no. of lines,words,unique words and the top words
     parameter=url"""

    html_content=get_html_content(url)
    data = parse_html_using_tag(html_content,'p')
    statistics=get_statistics(data)
    display_statistics(statistics)


def display_statistics(statistics):
    """To display the no. of lines,words,unqiue words,top 5 words
    parameter=statistics"""

    window['output'].Update('')
    window['output'].print("The web page contain following information\n")
    window['output'].print(statistics['line count'],"sentence")
    window['output'].print(statistics['words count'],"words")
    window['output'].print(statistics['unique words'],"unique words")
    window['output'].print("\nThe top words are\n")
    for words,count in statistics['top_words']:
        window['output'].print(words)


#https://www.edutopia.org/article/help-students-build-intrinsic-motivation
window=sg.Window("Web page analyzer",layout)

while True:
    event,values=window.Read()
    if event==sg.WINDOW_CLOSED:
        break
    elif event=="get":
        get_details(values['url'])


window.Close()
