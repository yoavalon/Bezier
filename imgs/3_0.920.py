d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.position_pen(0,1)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)
d.position_pen(1,3)

d.end()
