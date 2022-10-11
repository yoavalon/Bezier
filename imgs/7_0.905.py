d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,2)

d.end()
