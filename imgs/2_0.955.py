d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,0)
d.position_pen(2,1)
d.straight_line(Direction.SW, Length.short)

d.end()
