d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.medium)

d.end()
