d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.NE, Length.medium)

d.end()
