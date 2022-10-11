d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.medium)
d.position_pen(2,2)
d.position_pen(2,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
