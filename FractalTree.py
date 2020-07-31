import turtle as tu
root=tu.Turtle()
root.screen.bgcolor('orange')
root.left(90)
root.speed(20)
root.color('black')
root.pensize(5)
root.screen.title("Fractal Tree")
def fractal_tree_draw(b):
    if(b<10):
        return
    else:
        root.forward(b)
        root.left(30)
        fractal_tree_draw(3*b/4)
        root.right(60)
        fractal_tree_draw(3*b/4)
        root.left(30)
        root.backward(b)
fractal_tree_draw(80)
root=tu.done()
