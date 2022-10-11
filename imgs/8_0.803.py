d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(0,0)
d.straight_line(Direction.W, Length.long)

d.end()
