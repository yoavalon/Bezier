d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,2)
d.straight_line(Direction.W, Length.long)
d.position_pen(2,3)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)

d.end()
