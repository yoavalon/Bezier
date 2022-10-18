d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.E, Orient.right, Length.short, Radius.low)
d.curve(Direction.E, Orient.right, Length.short, Radius.low)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(2,1)

d.end()
