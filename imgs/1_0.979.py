d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.S, Length.medium)
d.position_pen(0,1)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.SW, Length.long)

d.end()
