d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.W, Length.medium)
d.position_pen(0,1)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.position_pen(1,0)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)

d.end()
