d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.position_pen(2,2)

d.end()
