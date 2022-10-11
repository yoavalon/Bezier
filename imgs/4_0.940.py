d = DslBezier()

d.position_pen(1,2)
d.position_pen(2,2)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)

d.end()
