d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NW, Orient.left, Length.long, Radius.low)
d.curve(Direction.S, Orient.right, Length.long, Radius.high)
d.position_pen(0,0)
d.position_pen(1,1)

d.end()
