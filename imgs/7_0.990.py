d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NW, Length.short)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)

d.end()
