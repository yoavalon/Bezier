d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.N, Length.medium)

d.end()
