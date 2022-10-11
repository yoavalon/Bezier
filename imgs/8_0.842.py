d = DslBezier()

d.position_pen(1,1)
d.position_pen(3,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(0,2)
d.straight_line(Direction.SW, Length.medium)

d.end()
