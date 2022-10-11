d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.long)
d.position_pen(0,1)

d.end()
