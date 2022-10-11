d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)

d.end()
