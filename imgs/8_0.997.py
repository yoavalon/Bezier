d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.position_pen(0,0)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,1)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.E, Length.medium)

d.end()
