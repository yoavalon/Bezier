d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.position_pen(0,2)
d.straight_line(Direction.S, Length.long)

d.end()
