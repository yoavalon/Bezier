d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.NW, Length.long)
d.position_pen(1,1)

d.end()
