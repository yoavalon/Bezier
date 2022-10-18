d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.N, Length.medium)
d.position_pen(2,0)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.position_pen(2,3)

d.end()
