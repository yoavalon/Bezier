d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.SE, Length.short)

d.end()
