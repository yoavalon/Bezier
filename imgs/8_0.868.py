d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.position_pen(3,2)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,3)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)

d.end()
