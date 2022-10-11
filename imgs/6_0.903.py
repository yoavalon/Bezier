d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.S, Length.long)
d.position_pen(2,1)

d.end()
