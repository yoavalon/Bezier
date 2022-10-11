d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.position_pen(1,1)

d.end()
