d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.high)
d.position_pen(1,2)

d.end()
