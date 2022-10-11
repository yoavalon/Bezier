d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(0,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.E, Length.long)

d.end()
