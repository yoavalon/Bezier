d = DslBezier()

d.position_pen(3,0)
d.straight_line(Direction.SE, Length.short)
d.position_pen(0,1)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)

d.end()
