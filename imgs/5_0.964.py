d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.W, Length.short)
d.position_pen(1,0)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)

d.end()
