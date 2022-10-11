d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.position_pen(0,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)

d.end()
