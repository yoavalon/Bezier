d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.W, Length.medium)

d.end()
