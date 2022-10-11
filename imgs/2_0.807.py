d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.W, Length.medium)

d.end()
