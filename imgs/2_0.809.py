d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.S, Length.long)
d.position_pen(3,0)
d.straight_line(Direction.NE, Length.short)

d.end()
