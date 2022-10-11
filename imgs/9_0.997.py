d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.curve(Direction.N, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.position_pen(1,3)

d.end()
