d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.SW, Length.long)
d.position_pen(2,1)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)

d.end()
