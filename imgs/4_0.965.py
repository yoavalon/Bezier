d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.short)
d.position_pen(2,2)
d.straight_line(Direction.SE, Length.long)
d.position_pen(1,2)

d.end()
