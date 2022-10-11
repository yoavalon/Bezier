d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.position_pen(3,1)
d.curve(Direction.NE, Orient.right, Length.long, Radius.high)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.position_pen(1,2)

d.end()
