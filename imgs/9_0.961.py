d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.N, Orient.right, Length.long, Radius.high)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.position_pen(3,1)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,3)

d.end()
