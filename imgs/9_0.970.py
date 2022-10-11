d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.position_pen(2,3)

d.end()
