d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.E, Length.long)
d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.position_pen(0,2)

d.end()
