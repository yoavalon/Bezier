d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.position_pen(3,1)
d.straight_line(Direction.N, Length.medium)
d.position_pen(1,3)
d.curve(Direction.SE, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.right, Length.short, Radius.low)

d.end()
