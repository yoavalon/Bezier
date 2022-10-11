d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)
d.position_pen(0,0)
d.curve(Direction.NW, Orient.right, Length.long, Radius.low)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.position_pen(3,2)

d.end()
