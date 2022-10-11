d = DslBezier()

d.position_pen(2,2)
d.position_pen(1,1)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.short)

d.end()
