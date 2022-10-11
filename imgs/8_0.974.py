d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NE, Length.long)
d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)

d.end()
