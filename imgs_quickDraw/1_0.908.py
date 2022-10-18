d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.S, Length.medium)
d.position_pen(3,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,1)

d.end()
