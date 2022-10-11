d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.S, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.position_pen(2,1)
d.straight_line(Direction.E, Length.medium)

d.end()
