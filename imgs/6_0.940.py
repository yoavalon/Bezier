d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.position_pen(2,1)

d.end()
