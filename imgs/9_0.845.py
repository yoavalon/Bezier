d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.low)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)

d.end()
