d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.N, Length.long)
d.straight_line(Direction.SW, Length.long)
d.position_pen(1,1)

d.end()
