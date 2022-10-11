d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,1)

d.end()
