d = DslBezier()

d.position_pen(1,2)
d.position_pen(3,0)
d.straight_line(Direction.SE, Length.long)
d.position_pen(1,1)
d.curve(Direction.N, Orient.left, Length.short, Radius.low)

d.end()
