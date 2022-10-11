d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)

d.end()
