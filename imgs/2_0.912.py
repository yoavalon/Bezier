d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.position_pen(2,0)
d.straight_line(Direction.N, Length.long)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.NE, Length.medium)

d.end()
