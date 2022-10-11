d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.W, Length.short)

d.end()
