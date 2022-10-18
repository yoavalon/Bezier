d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.SW, Length.medium)

d.end()
