d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.short, Radius.low)
d.position_pen(2,2)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.NE, Length.short)

d.end()
