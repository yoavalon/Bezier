d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.SE, Length.medium)

d.end()
