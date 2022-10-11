d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)

d.end()
