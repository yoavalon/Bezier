d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.position_pen(3,3)
d.straight_line(Direction.SW, Length.short)

d.end()
