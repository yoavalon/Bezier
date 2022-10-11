d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(0,1)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.position_pen(1,1)

d.end()
