d = DslBezier()

d.position_pen(1,3)
d.position_pen(1,0)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)

d.end()
