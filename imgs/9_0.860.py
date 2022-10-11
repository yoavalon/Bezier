d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.W, Length.short)
d.position_pen(2,0)

d.end()
