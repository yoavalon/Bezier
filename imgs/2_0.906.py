d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SW, Length.short)
d.position_pen(0,3)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.low)
d.position_pen(1,0)

d.end()
