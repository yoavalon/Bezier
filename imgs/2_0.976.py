d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.long)
d.position_pen(1,2)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)

d.end()
