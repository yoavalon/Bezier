d = DslBezier()

d.position_pen(2,3)
d.position_pen(0,0)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.position_pen(3,1)

d.end()
