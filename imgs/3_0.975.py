d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.short)
d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.position_pen(1,0)

d.end()
