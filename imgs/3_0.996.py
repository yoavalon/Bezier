d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.position_pen(1,2)
d.straight_line(Direction.NW, Length.long)
d.position_pen(1,0)

d.end()
