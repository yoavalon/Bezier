d = DslBezier()

d.position_pen(1,1)
d.position_pen(3,0)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)

d.end()
