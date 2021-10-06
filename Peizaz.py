import graphics as gr

window = gr.GraphWin("Красивый пейзаж", 800, 600)

# Небо
nebo = gr.Rectangle(gr.Point(0, 0), gr.Point(800, 300))     
nebo.setFill('blue')

# Домик тело
Dom = gr.Rectangle(gr.Point(200, 200), gr.Point(400, 400))     
Dom.setFill('grey')
Dom.setWidth(4)
# Домик окно
okno = gr.Rectangle(gr.Point(250, 250), gr.Point(350, 350))     
okno.setFill('yellow')
okno.setWidth(4)
rama1 = gr.Line(gr.Point(300, 250), gr.Point(300,350))
rama1.setWidth(4)
rama2 = gr.Line(gr.Point(250, 300), gr.Point(350,300))
rama2.setWidth(4)
# Домик крыша

# Солнце
Sol = gr.Circle(gr.Point(600, 100), 50)
Sol.setFill('yellow')
# Ёлка

# Облака





# Отрисовака

nebo.draw(window)
Dom.draw(window)
okno.draw(window)
rama1.draw(window)
rama2.draw(window)


Sol.draw(window)

window.getMouse()

window.close()

'''
face = gr.Circle(gr.Point(200, 200), 100)
face.setFill('yellow')

eye1 = gr.Circle(gr.Point(150, 180), 20)
eye2 = gr.Circle(gr.Point(250, 180), 15)
eye1_center = gr.Circle(gr.Point(150, 180), 8)
eye2_center = gr.Circle(gr.Point(250, 180), 7)
eye1.setFill('red')
eye2.setFill('red')
eye1_center.setFill('black')
eye2_center.setFill('black')

eyebrow1 = gr.Line(gr.Point(100, 120), gr.Point(180, 170))
eyebrow2 = gr.Line(gr.Point(220, 170), gr.Point(300, 140))
eyebrow1.setWidth(10)
eyebrow2.setWidth(10)
eyebrow1.setOutline('black')
eyebrow2.setOutline('black')

mouth = gr.Line(gr.Point(150, 260), gr.Point(250, 260))
mouth.setWidth(20)
mouth.setOutline('black')

face.draw(window)
eye1.draw(window)
eye2.draw(window)
eye1_center.draw(window)
eye2_center.draw(window)
eyebrow1.draw(window)
eyebrow2.draw(window)
mouth.draw(window)

window.getMouse()

window.close()
'''
