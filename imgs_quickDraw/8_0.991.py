d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.SW, Orient.left, Length.long, Radius.low)
d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
