d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(0,2)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
