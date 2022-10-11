d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.short)
d.position_pen(2,0)
d.position_pen(0,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.low)

d.end()
