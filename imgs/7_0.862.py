d = DslBezier()

d.position_pen(3,3)
d.position_pen(0,3)
d.straight_line(Direction.SW, Length.long)
d.position_pen(2,3)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.curve(Direction.NW, Orient.left, Length.long, Radius.low)

d.end()
