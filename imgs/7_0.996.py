d = DslBezier()

d.position_pen(2,1)
d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.short)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)

d.end()
