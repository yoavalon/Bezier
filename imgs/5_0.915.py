d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.W, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.SE, Length.short)
d.position_pen(2,2)

d.end()
