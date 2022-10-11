d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
