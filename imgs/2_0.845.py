d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.SE, Orient.left, Length.short, Radius.low)
d.curve(Direction.N, Orient.right, Length.long, Radius.medium)
d.position_pen(0,0)

d.end()
