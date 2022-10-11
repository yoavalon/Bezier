d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.position_pen(1,3)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.position_pen(1,2)

d.end()
