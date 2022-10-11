d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.position_pen(0,1)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,3)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)

d.end()
