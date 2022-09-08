d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,0)
d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)

d.end()
