d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(3,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)

d.end()
