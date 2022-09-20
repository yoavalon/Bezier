d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(3,2)

d.end()
