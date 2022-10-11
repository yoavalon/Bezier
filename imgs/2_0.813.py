d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.S, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)

d.end()
