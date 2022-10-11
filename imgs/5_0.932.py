d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,3)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.SE, Length.short)
d.position_pen(3,2)

d.end()
