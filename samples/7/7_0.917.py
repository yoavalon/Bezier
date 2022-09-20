d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)
d.position_pen(0,1)
d.straight_line(Direction.SW, Length.long)
d.position_pen(1,1)
d.position_pen(1,0)

d.end()
